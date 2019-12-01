#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String, Int8

class emotionListener:

	shift = None
	
	def __init__(self):

		self.emotionSub = rospy.Subscriber("/QTInstrument/emotion", Int8, self.emotionCallback)

	def emotionCallback(self, data):
		
		self.shift = data.data
		print(self.shift)

class noteShifter:

	note = None
	shift = emotionListener()

	def __init__(self):

		self.musicSub = rospy.Subscriber("/QTInstrument/music", String, self.noteCallback)
		self.musicPub = rospy.Publisher("/qt_robot/audio/play", String, queue_size=1)

	def noteCallback(self, data):
		
		path = "QT/"
		extention = ".wav"

		self.note = data.data
		self.shiftNote() #Shift the note if necessary
		fileName = path + self.note + extension
		self.musicPub.publish(fileName)

	def shiftNote(self):

		shift = self.shift.shift

		if shift == None:
			return		

		#Math to shift note

		noteN = ord(self.note[0]) - 65 #Ranges from A to G

		if len(self.note) == 2: #If no semitone
			octaveN = int(self.note[1])
		else if len(self.note) == 3: #If semitone
			semitone = self.note[1]
			octaveN = int(self.note[2])
		else:
			return #Something is wrong with the note received

		newNoteN = (noteN + shift) % 7
		newNoteStr = chr(newNoteN + 65)
		
		if semitone:
			newNoteStr = newNoteStr + semitone			
			if newNoteStr == "E#":
				newNoteStr = "F" # E# is the same as F
			else if newNoteStr == "B#":
				newNoteStr = "C" # B# is the same as C

		realIncrement = (noteN - 2) % 7 + shift # -2 and %7 because C is 2 but should be 0 for real increment and A is 0 but should be 5 for real increment etc.

		if realIncrement > 7: #In case we reach one octave higher
			octaveN += 1
		else if realIncrement < 0: #Reach one octave lower
			octaveN -= 1
		
		self.note = newNoteStr + str(octaveN)

def main():

	note = noteShifter()

	rospy.init_node('emotionConverter', anonymous=True)

	try:

		rospy.spin()

	except KeyboardInterrupt:

		print("Shutting down...")

main()


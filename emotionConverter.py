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

		noteN = ord(self.note[0]) - 65

		if len(self.note) == 2:
			octaveN = int(self.note[1])
		else if len(self.note) == 3:
			semitone = self.note[1]
			octaveN = int(self.note[2])
		else:
			return #Something is wrong with the note received

		newNoteN = (noteN + shift) % 7
		realIncrement = (noteN - 2) % 7 + shift

		if realIncrement > 7: #In case we reach one octave higher
			octaveN += 1
		else if realIncrement < 0: #Reach one octave lower
			octaveN -= 1

		if semitone:
			self.note = chr(newNoteN + 65) + semitone + str(octaveN)
		else:
			self.note = chr(newNoteN + 65) + str(octaveN)

def main():

	note = noteShifter()

	rospy.init_node('emotionConverter', anonymous=True)

	try:

		rospy.spin()

	except KeyboardInterrupt:

		print("Shutting down...")

main()


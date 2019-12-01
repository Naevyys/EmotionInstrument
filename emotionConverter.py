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
		self.shiftNote()
		fileName = path + self.note + extension
		self.musicPub.publish(fileName)

	def shiftNote(self):

		shift = self.shift.shift

		if shift == None:
			return		

		#Math to shift note
		octaveN = self.note[1]
		noteN = ord(self.note[0]) - 65
		newNoteN = (n + shift) % 7
		self.note = chr(newN + 65) + octaveN

def main():

	emotion = emotionListener()

	rospy.init_node('emotionConverter', anonymous=True)

	try:

		rospy.spin()

	except KeyboardInterrupt:

		print("Shutting down...")

main()


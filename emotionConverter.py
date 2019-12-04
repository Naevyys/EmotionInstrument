#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String, Int8, Int16

class emotionListener:

	shift = None
	
	def __init__(self):

		self.emotionSub = rospy.Subscriber("/QTInstrument/emotion", Int8, self.emotionCallback)

	def emotionCallback(self, data):
		
		self.shift = data.data
		print(self.shift)

class noteShifter:

	note = None
	octave = None
	shift = emotionListener()
	extension = '.wav'

	def __init__(self):

		self.musicSub = rospy.Subscriber("/QTInstrument/music", Int16, self.noteCallback)
		self.musicPub = rospy.Publisher("/qt_robot/audio/play", String, queue_size=1)

	def noteCallback(self, data):

		self.note = data.data % 100 #Extract two last digits
		self.octave = data.data // 100 #Extract hundreds
		(noteStr, octaveStr) = self.shiftNote() #Shift the note and octave if necessary
		path = 'Octaves/Octave' + octaveStr + "/"
		fileName = path + noteStr + self.extension
		#self.musicPub.publish(fileName)
		print(fileName)

	def shiftNote(self):
		
		shift = self.shift.shift

		if shift == None:
			return (str(self.note), str(self.octave))
		
		n = self.note + shift
		
		if n < 0:
			self.octave -= 1
		elif n > 12:
			self.octave += 1

		self.note = n % 12

		return (str(self.note), str(self.octave))

def main():

	note = noteShifter()

	rospy.init_node('emotionConverter', anonymous=True)

	try:

		rospy.spin()

	except KeyboardInterrupt:

		print("Shutting down...")

main()


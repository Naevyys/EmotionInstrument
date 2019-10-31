#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String

class emotionListener:

	emotion = None
	
	def __init__(self):

		self.emotionSub = rospy.Subscriber("/QTInstrument/emotion", String, self.emotionCallback)

	def emotionCallback(self, data):
		
		self.emotion = data.data
		print(self.emotion)

def main():

	emotion = emotionListener()

	rospy.init_node('emotionConverter', anonymous=True)

	try:

		rospy.spin()

	except KeyboardInterrupt:

		print("Shutting down...")

main()


#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class noteSender:

	note = None

	def __init__(self):

		self.musicPub = rospy.Publisher("/QTInstrument/music", String, queue_size=1)

	def sendMusic(self):

		self.note = "C3"
		self.musicPub.publish(self.note)

def main():

	music = noteSender()

	rospy.init_node('musicPub', anonymous=True)

	rate = ropsy.Rate(1)

	try:

		while not rospy.is_shutdown():
			music.sendMusic()
			rate.sleep()

	except KeyboardInterrupt:

		print("Shutting down...")


#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

class noteSender:

	note = None

	def __init__(self):

		self.musicPub = rospy.Publisher("/QTInstrument/music", Int16, queue_size=1)

	def sendMusic(self):

		self.note = 403 #Octave 4, note D major, just as an example
		self.musicPub.publish(self.note)	

def main():

	music = noteSender()

	rospy.init_node('musicPub', anonymous=True)

	rate = rospy.Rate(2.5)

	try:

		while not rospy.is_shutdown():
			music.sendMusic()
			rate.sleep()

	except KeyboardInterrupt:

		print("Shutting down...")

main()

#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import Int8
from sensor_msgs.msg import Image
from qt_nuitrack_app.msg import Faces
from cv_bridge import CvBridge, CvBridgeError

class emotionAnalyser:

	face = None
	emotion = None
	shift = None

	def __init__(self):

		self.facesSub = rospy.Subscriber("qt_nuitrack_app/faces", Faces, self.faceCallback)
		self.emotionPub = rospy.Publisher("/QTInstrument/emotion", Int8, queue_size=1)

	def faceCallback(self, data):

		self.face = data.faces[0]

		(self.emotion, self.shift) = self.findEmotion(self.face)
		print(self.emotion)
		self.emotionPub.publish(self.shift)

	def findEmotion(self, face):

		neutral = face.emotion_neutral
		angry = face.emotion_angry
		happy = face.emotion_happy
		surprise = face.emotion_surprise

		emotionArray = [(neutral, 0, "neutral"), (angry, 1, "angry"), (happy, 2, "happy"), (surprise, 3, "surprise")]

		top = 0
		emotion = None
		shift = None

		for i in range(len(emotionArray)):
			if top < emotionArray[i][0]:
				top = emotionArray[i][0]
				emotion = emotionArray[i][2]
				shift = emotionArray[i][1]

		return (emotion, shift)
	

class imageView:

	def __init__(self):

		self.imageSub = rospy.Subscriber("/camera/color/image_raw", Image, self.imageCallback)

	def imageCallback(self, data):

		self.bridge = CvBridge()

		try:

			cvImage = self.bridge.imgmsg_to_cv2(data, "bgr8")

		except CvBridgeError as e:

			print(e)

		cv2.imshow("Image View", cvImage)
		cv2.waitKey(1)


def main():

	image = imageView()
	emotion = emotionAnalyser()

	rospy.init_node('emotionReader', anonymous=True)

	try:

		rospy.spin()

	except KeyboardInterrupt:

		print("Shutting down...")

	cv2.destroyAllWindows()

main()


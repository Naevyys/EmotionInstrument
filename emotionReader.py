#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from qt_nuitrack_app.msg import Faces
from cv_bridge import CvBridge, CvBridgeError

class emotionAnalyser:

	face = None
	expression = None

	def __init__(self):

		self.facesSub = rospy.Subscriber("qt_nuitrack_app/faces", Faces, self.faceCallback)

	def faceCallback(self, data):

		self.face = data.faces[0]
		self.FacialExpression = findEmotion(self.face)

	def findEmotion(self, face):

		neutral = face.emotion_neutral
		angry = face.emotion_angry
		happy = face.emotion_happy
		surprise = face.emotion_surprise

		emotionArray = [[neutral, "neutral"], [angry, "angry"], [happy, "happy"], [surprise, "surprise"]]

		top = 0
		emotion = None

		for i in range(4):
			if top < emotionArray[i][0]:
				emotion = emotionArray[i][1]

		return emotion
	
	def getEmotion(self):

		return self.facialExpression

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


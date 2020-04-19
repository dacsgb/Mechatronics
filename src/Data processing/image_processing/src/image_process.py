#!/usr/bin/env python2

import sys

import numpy as np

import rospy
import cv2

from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError

#--- Define our Class
class Node():

    def __init__(self):
        # Set up code variables
        self.mask = np.array([[0,100,0],[255,255,180]])

        # Publisher of the original frame
        self.orig_pub = rospy.Publisher("/image_processor/original",Image,queue_size=1)

        # Publisher of the modifiend frame
        #self.grey_pub = rospy.Publisher("/image_processor/grey",Image,queue_size=1)
        #self.masked_pub = rospy.Publisher("/image_processor/masked",Image,queue_size=1)

        self.grey_pub = rospy.Publisher("/image_processor/grey",Image,queue_size=1)

        self.masked_pub = rospy.Publisher("/image_processor/masked",Image,queue_size=1)

        # Subscriber to the camera flow
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/compressed",CompressedImage,self.callback)

    def callback(self,msg):
        print("recieved")
        self.cv_orig = cv2.imdecode(np.fromstring(msg.data, np.uint8), cv2.IMREAD_COLOR)

        self.process()
        self.pub()

    def pub(self):

        self.orig_pub.publish(self.bridge.cv2_to_imgmsg(self.cv_orig, "bgr8"))

        self.grey_pub.publish(self.bridge.cv2_to_imgmsg(self.grey_data, "8UC1"))

        self.masked_pub.publish(self.bridge.cv2_to_imgmsg(self.masked_data, "bgr8"))
        print("published")

    def process(self):
        self.grey_data = cv2.cvtColor(self.cv_orig, cv2.COLOR_BGR2GRAY)

        self.hsv = cv2.cvtColor(self.cv_orig, cv2.COLOR_BGR2HSV)

        self.masked_data = cv2.cvtColor(cv2.bitwise_and(self.hsv,self.hsv, mask=cv2.inRange(self.hsv, self.mask[0], self.mask[1])), cv2.COLOR_HSV2BGR)



    def run(self):
        while not rospy.is_shutdown():
            pass

if __name__ == '__main__':
    rospy.init_node("image_processor")
    Processor = Node()
    Processor.run()
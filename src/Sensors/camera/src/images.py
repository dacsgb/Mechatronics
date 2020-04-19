#!/usr/bin/env python2

import sys

import numpy as np

import rospy
import cv2

from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError

class Node():
    def __init__(self,fps):
        self.image_pub = rospy.Publisher("/camera/original",Image,queue_size=1)

        self.compressed_pub = rospy.Publisher("/camera/compressed",CompressedImage,queue_size=1)
        self.comp_img = CompressedImage()

        self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        
        self.bridge = CvBridge()

        self.cap = cv2.VideoCapture(0)

        self.rate = rospy.Rate(fps)

    def run(self):
        while not rospy.is_shutdown():
            _, frame = self.cap.read()

            self.image_pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))

            self.comp_img.header.stamp = rospy.Time.now()
            self.comp_img.format = "jpeg"
            self.comp_img.data = np.array(cv2.imencode('.jpg', frame)[1]).tostring()
            self.compressed_pub.publish(self.comp_img)

            self.rate.sleep()
    
if __name__ == "__main__":
    rospy.init_node("camera")
    Camera = Node(15)
    Camera.run()

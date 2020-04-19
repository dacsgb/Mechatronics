#!/usr/bin/env python
import numpy as np

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class Node():
    def __init__(self):
        self.cmd = Twist()

        self.speed_max = 5.2359*0.0665
        self.omega_max = self.speed_max/
        self.threshold = 0.05

        self.joints_pub = rospy.Publisher("/servo_cmd",Twist,queue_size=1)
        self.joy_sub = rospy.Subscriber("joy", Joy, self.remote_cb)
        self.rate = rospy.Rate(100)

    def remote_cb(self,message):
        if abs(message.axes[0]) >= self.threshold:
            self.cmd.linear.x = self.speed_max*message.axes[0]
        else:
            self.cmd.linear.x = 0
        if abs(message.axes[1]) >= self.threshold:
            self.cmd.angular.z = self.omega_max*message.axes[1]
        else:
            self.cmd.angular.z = 0

    def run(self):
        while not rospy.is_shutdown():
            self.joints_pub.publish(self.cmd)
            self.rate.sleep()

if __name__ == "__main__":
    rospy.init_node('joy_to_rover')
    Teleop = Node()
    Teleop.run()
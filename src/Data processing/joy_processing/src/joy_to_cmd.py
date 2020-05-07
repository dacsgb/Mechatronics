#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class Node():
    def __init__(self,speed,omega,longi,angular,thres):
        self.cmd = Twist()

        self.speed_max = speed
        self.omega_max = omega
        self.threshold = thres
        self.longi = longi
        self.angular = angular

        self.joints_pub = rospy.Publisher("/servo_cmd",Twist,queue_size=1)
        self.joy_sub = rospy.Subscriber("/joystick", Joy, self.remote_cb)
        self.rate = rospy.Rate(100)

    def remote_cb(self,message):
        if abs(message.axes[self.longi]) >= self.threshold:
            self.cmd.linear.x = self.speed_max*message.axes[1]
        else:
            self.cmd.linear.x = 0
        if abs(message.axes[self.angular]) >= self.threshold:
            self.cmd.angular.z = self.omega_max*message.axes[0]
        else:
            self.cmd.angular.z = 0

    def run(self):
        while not rospy.is_shutdown():
            self.joints_pub.publish(self.cmd)
            self.rate.sleep()

if __name__ == "__main__":
    rospy.init_node('joy_to_rover')

    speed = rospy.get_param('~v_max')
    omega = rospy.get_param('~omega_max')
    thres = rospy.get_param('~threshold')
    longi = rospy.get_param('~longi')
    angular = rospy.get_param('~angular')

    Teleop = Node(speed,omega,longi,angular,thres)
    Teleop.run()
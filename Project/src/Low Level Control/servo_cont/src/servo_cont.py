#!/usr/bin/env python

import time
import numpy as np

from Hat import DFRobot_Expansion_Board_IIC as Board
from Hat import DFRobot_Expansion_Board_Servo as Servo

import rospy
from geometry_msgs.msg import Twist

class Node():
    def __init__(self):
        self.board = Board(1, 0x10)
        self.servo = Servo(self.board,[90,90,90,90])
        
        self.omegas = np.array([0,0,0,0])
        self.J = np.array([[1,-1],[1,-1],[-1,1],[-1,1]])

        self.remote_sub = rospy.Subscriber("/servo_cmd",Twist,self.remote_cb)
        self.rate = rospy.Rate(1000)

    def remote_cb(self,message):
        u = np.array([message.linear.x,message.angular.z])
        self.omegas = np.dot(self.J,u)
        print(self.omegas)

    def run(self):
        while not rospy.is_shutdown():
            self.servo.act(self.omegas)
            self.rate.sleep()

if __name__ == "__main__":
    rospy.init_node('servo_cont')
    Servos = Node()
    Servos.run()
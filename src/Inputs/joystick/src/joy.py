#!/usr/bin/python

import pygame

import rospy 
from sensor_msgs.msg import Joy

class Node():
    def __init__(self):

        self.stick = pygame.joystick.Joystick(0)
        self.stick.init()

        self.rate = rospy.Rate(50)

        self.joy_pub = rospy.Publisher("/joystick",Joy,queue_size=1)

        self.msg = Joy()
        self.msg.axes = [0]*self.stick.get_numaxes()
        self.msg.buttons = [0]*(self.stick.get_numbuttons()+2)

    def fill(self):
        self.msg.header.stamp = rospy.Time.now()

        for i in range(0,len(self.msg.axes)):
            self.msg.axes[i]= self.stick.get_axis(i)
        
        for i in range(0,len(self.msg.buttons)-2):
            self.msg.buttons[i] = self.stick.get_button(i)

        self.msg.buttons[-2] = self.stick.get_hat(0)[0]
        self.msg.buttons[-1] = self.stick.get_hat(0)[1]

    def pub(self):
        self.joy_pub.publish(self.msg)

    def run(self):
        while not rospy.is_shutdown():
            pygame.event.pump() 
            self.fill()
            self.pub()
            self.rate.sleep()


if __name__ == "__main__":
    rospy.init_node("joystick")
    pygame.init()
    Controller = Node()
    Controller.run()

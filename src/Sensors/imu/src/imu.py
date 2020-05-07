#!/usr/bin/env python

from mpu6050 import mpu6050

import rospy
from sensor_msgs.msg import Imu

class Node():
    def __init__(self,add):
        self.imu = mpu6050(add)
        self.msg = Imu()
        
        self.rate = rospy.Rate(100)
        self.imu_pub = rospy.Publisher('/imu',Imu,queue_size=1)

    def fill_msg(self):
        self.msg.header.stamp = rospy.Time.now()
        self.msg.header.frame_id = 'imu'

        self.msg.orientation.w = 0
        self.msg.orientation.x = 0
        self.msg.orientation.y = 0
        self.msg.orientation.z = 0
        self.msg.orientation_covariance[0] = -1

        accel_data = self.imu.get_accel_data()
        self.msg.linear_acceleration.x = accel_data['x']
        self.msg.linear_acceleration.y = accel_data['y']
        self.msg.linear_acceleration.z = accel_data['z']
        self.msg.linear_acceleration_covariance[0] = -1

        gyro_data = self.imu.get_gyro_data()
        self.msg.angular_velocity.x = gyro_data['x']
        self.msg.angular_velocity.y = gyro_data['y']
        self.msg.angular_velocity.z = gyro_data['z']
        self.msg.angular_velocity_covariance[0] = -1
    
    def run(self):
        while not rospy.is_shutdown():

            self.fill_msg()
            self.imu_pub.publish(self.msg)
            self.rate.sleep()

if __name__ == "__main__":
    rospy.init_node("IMU")
    Sensor = Node(0x68)
    Sensor.run()


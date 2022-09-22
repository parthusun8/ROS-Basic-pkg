#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



def pose_callback():
	rospy.loginfo("Moving in a circle : %f",msg.x)
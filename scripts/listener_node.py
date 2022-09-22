#!/usr/bin/env python


import rospy
from pkg_ros_basics.msg import my_msg



def func_callback_topic_my_topic(my_msg):


	rospy.loginfo("Data Received: (%d, %s, %.2f, %.2f)",
		my_msg.id,my_msg.name,my_msg.temperature,my_msg.humidity)


def main():
		#1. Initialize the suscriber node
		rospy.init_node('listener_node', anonymous=True)

		#2. Suscribe to the desired topic and attach a Callback Function to it
		rospy.Subscriber("my_topic", my_msg,func_callback_topic_my_topic)

		#3. spin() simply keeps python from exiting until this node is stopped
		rospy.spin()

#Python Main
if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass

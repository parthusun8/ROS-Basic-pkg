#!/usr/bin/env python


import rospy
from pkg_ros_basics.msg import my_msg


import random



def main():
	#1. Create a handle to publish messages to a topic
	var_handle_pub = rospy.Publisher('my_topic',my_msg,queue_size=10)

	#2. Initializes the ROS node for the process
	rospy.init_node('talker_node', anonymous=True)

	#3. Set the Loop Rate
	var_loop_rate = rospy.Rate(1) #Loop will do its best to run 1 time in 1 second #1Hz

	#4. Write the infinite Loop
	while not rospy.is_shutdown():
		obj_msg = my_msg()

		obj_msg.id = 1
		obj_msg.name = "PARTH"
		obj_msg.temperature = 10 + random.random()


		rospy.loginfo("Publishing : ")
		rospy.loginfo(obj_msg)


		var_handle_pub.publish(obj_msg)
		var_loop_rate.sleep()

#Python main
if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass

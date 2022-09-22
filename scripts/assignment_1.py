#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def pose_callback(msg) :
	rospy.loginfo("Moving in a circle : \n%f",msg.x) 


def draw_circle_once():

	#1. Initializes the ROS node for the process
	rospy.init_node('turtle_revolve', anonymous=True)

	#2. Create a handle to publish messages to a topic
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

	#3. Set the Loop Rate
	var_loop_rate = rospy.Rate(10) #Loop will do its best to run 10 time in 1 second #1Hz


	rospy.Subscriber("/turtle1/pose", Pose, pose_callback)

	vel_msg = Twist()
	
	vel_msg.linear.x = 1.0
	vel_msg.angular.z = 1.0
	radius = (vel_msg.linear.x) / (vel_msg.angular.z)
	circumference = 2 * 3.14 * radius

	now = rospy.Time.now().to_sec()

	#print("RADIUS : %f \n CIRCUMFERENCE : %f",radius,circumference)
	#4. Write the infinite Loop
	while not rospy.is_shutdown():

		then = rospy.Time.now().to_sec()
		time_diff = then - now
		theta = vel_msg.angular.z * time_diff

		if theta >= circumference : 
			rospy.loginfo("Goal Reached ")
			break
		#print(then - now)
		velocity_publisher.publish(vel_msg)


		var_loop_rate.sleep()

		
#Python main
if __name__ == '__main__':
	try:
		draw_circle_once()
	except rospy.ROSInterruptException:
		pass

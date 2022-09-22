#!/usr/bin/env python


import rospy


def main() :
	#1. Make the script a ROS node.
	rospy.init_node('param_get_set',anonymous=True)

	#2. Read from Parameter server
	rospy.loginfo("Reading from Parameter server")

	#3. Get all the parameters inside 'details'
	param_config_my = rospy.get_param('Details')

	#4.	Store the values in Variables
	first_name = param_config_my['Name']['first']
	last_name = param_config_my['Name']['last']
	address = param_config_my['Contact']['Address']
	phone = param_config_my['Contact']['Phone']

	#5. Print the parameters
	rospy.loginfo(">> First Name: {}".format(first_name))
	rospy.loginfo(">>Last Name: {}".format(last_name))
	rospy.loginfo(">> Address: {}".format(address))
	rospy.loginfo(">> Phone: {}".format(phone))

	#6.	Modifying a value

	#Modifying Phone number
	rospy.set_param('/Details/Contact/Phone',"9078083651")
	new_Phone = rospy.get_param('/Details/Contact/Phone')

	rospy.loginfo(">> New Phone: {}".format(new_Phone))

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
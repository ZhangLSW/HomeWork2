#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String

if __name__ == '__main__':
	rospy.init_node('talker')
	pub = rospy.Publisher('talker_up',String,queue_size=10)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		message =  "%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		pub.publish(message)
		rate.sleep()

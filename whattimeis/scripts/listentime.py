#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String

m=''

def cb(message):
	#print message.data
	global m
	m=message.data

if __name__ == '__main__':
	rospy.init_node('lister')
	sub = rospy.Subscriber('talker_up',String,cb)
	pub = rospy.Publisher('lister', String, queue_size=10) 
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
        	m= "%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                pub.publish(m)
                rate.sleep()

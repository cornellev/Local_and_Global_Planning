#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid

def find_path():
    x = "hawwo"
    rospy.loginfo(x)
    pub.publish(x)

if __name__ == '__main__':
    try:
	height = 800
	width = 800
	resolution = .25


        pub = rospy.Publisher('coords', String, queue_size=10)
        rospy.init_node('planning_node', anonymous=True)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
                find_path()
                rate.sleep()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

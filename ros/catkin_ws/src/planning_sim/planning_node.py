# !/usr/bin/env python3

import rospy
from std_msgs.msg import String

def find_path(data):
    x = "hawwo"
    pub.publish(x)

if __name__ == '__main__':
    try:
        rospy.init_node('planning_node', anonymous=True)
        pub = rospy.Publisher('coords', String, queue_size=1)
        # mappub = rospy.Publisher("/map", Map, find_path)
	# Sub to 2D nav goal here
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

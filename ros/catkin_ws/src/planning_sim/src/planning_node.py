#!/usr/bin/env python3

import rospy
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Header
import numpy as np

def find_path():
    pass

def grid_setup(data):
    grid = data.data

if __name__ == '__main__':
    try:
        grid = None
        target = None
        current_pose = None

        rospy.init_node('planning_node', anonymous=True)
        rospy.Subscriber("move_base_simple/goal", PoseStamped, lambda data: target = data.pose.position)
        rospy.Subscriber("", PoseStamped, lambda data: current_pose = data.pose.position)
        rospy.Subscriber("occupancy_grid", OccupancyGrid, lambda data: grid = data.data)
        rospy.Publisher("vector_path", Path, queue_size=1)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass

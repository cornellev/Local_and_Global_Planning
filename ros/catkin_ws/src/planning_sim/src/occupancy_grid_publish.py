#!/usr/bin/env python3

import rospy
import rospkg
from sensor_msgs.msg import Image
from nav_msgs.msg import OccupancyGrid
from PIL import Image as PILImage
import numpy as np

class ImageToOccupancyGrid:
    def __init__(self, img_src):
        rospy.init_node('image_to_occupancy_grid', anonymous=True)

        self.image_file = rospy.get_param('~image_file', img_src)
        self.resolution = rospy.get_param('~resolution', 0.05)  # meters per pixel
        self.origin_x = rospy.get_param('~origin_x', 0.0)  # meters
        self.origin_y = rospy.get_param('~origin_y', 0.0)  # meters

        # Load image
        self.image = PILImage.open(self.image_file).convert('L')

        # Publishers
        self.occupancy_grid_pub = rospy.Publisher('occupancy_grid', OccupancyGrid, queue_size=10)

    def convert_image_to_occupancy_grid(self):
        occupancy_grid = OccupancyGrid()

        occupancy_grid.header.stamp = rospy.Time.now()
        occupancy_grid.header.frame_id = 'map'
        occupancy_grid.info.resolution = self.resolution
        occupancy_grid.info.width = self.image.width
        occupancy_grid.info.height = self.image.height
        occupancy_grid.info.origin.position.x = self.origin_x
        occupancy_grid.info.origin.position.y = self.origin_y
        occupancy_grid.info.origin.position.z = 0.0
        occupancy_grid.info.origin.orientation.x = 0.0
        occupancy_grid.info.origin.orientation.y = 0.0
        occupancy_grid.info.origin.orientation.z = 0.0
        occupancy_grid.info.origin.orientation.w = 1.0

        # Convert black and white image to occupancy grid data
        occupancy_data = []
        for y in range(self.image.height):
            occupancy_row = []
            for x in range(self.image.width):
                pixel = self.image.getpixel((x, y))
                if pixel == 0:  # black pixel (occupied)
                    occupancy_row.append(100)
                else:  # white pixel (free)
                    occupancy_row.append(0)
            occupancy_data.append(occupancy_row)

        # Set occupancy grid data
        occupancy_grid.data = np.array(occupancy_data).flatten()

        return occupancy_grid

    def publish_occupancy_grid(self):
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            occupancy_grid = self.convert_image_to_occupancy_grid()
            self.occupancy_grid_pub.publish(occupancy_grid)
            rate.sleep()

if __name__ == '__main__':
    try:
        path = rospkg.RosPack().get_path('planning_sim')
        image_to_occupancy_grid = ImageToOccupancyGrid(path + '/src/image.png')
        image_to_occupancy_grid.publish_occupancy_grid()
    except rospy.ROSInterruptException:
        pass

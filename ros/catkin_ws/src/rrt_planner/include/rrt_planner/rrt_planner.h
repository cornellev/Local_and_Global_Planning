#include <ros/ros.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <costmap_2d/costmap_2d.h>
#include <nav_core/base_global_planner.h>
#include <geometry_msgs/PoseStamped.h>
#include <angles/angles.h>
#include <base_local_planner/world_model.h>
#include <base_local_planner/costmap_model.h>

using std::string;

#ifndef RRT_PLANNER_CPP
#define RRT_PLANNER_CPP

namespace rrt_planner {

  class RRTPlanner : public nav_core::BaseGlobalPlanner {
    public:

      costmap_2d::Costmap2DROS* costmap_ros;
      costmap_2d::Costmap2D* costmap;
      int size_x;
      int size_y;

      float threshold;

      RRTPlanner();
      RRTPlanner(std::string name, costmap_2d::Costmap2DROS* costmap_ros);

      void initialize(
        std::string name, 
        costmap_2d::Costmap2DROS* costmap_ros
      );

      void algorithm();

      bool checkObstacle(double x, double y);

      bool makePlan(
        const geometry_msgs::PoseStamped& start,
        const geometry_msgs::PoseStamped& goal,
        std::vector<geometry_msgs::PoseStamped>& plan
      );
  };
};
#endif
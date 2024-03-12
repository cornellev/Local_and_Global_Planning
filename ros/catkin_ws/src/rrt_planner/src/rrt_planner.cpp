#include <pluginlib/class_list_macros.h>
#include "rrt_planner/rrt_planner.h"

//register this planner as a BaseGlobalPlanner plugin
PLUGINLIB_EXPORT_CLASS(rrt_planner::RRTPlanner, nav_core::BaseGlobalPlanner)

using namespace std;

//Default Constructor
namespace rrt_planner {

  RRTPlanner::RRTPlanner (){}

  RRTPlanner::RRTPlanner(std::string name, costmap_2d::Costmap2DROS* costmap_ros) {
    initialize(name, costmap_ros);
  }

  void RRTPlanner::initialize(std::string name, costmap_2d::Costmap2DROS* costmap_ros) {
    this->costmap_ros = costmap_ros;
    this->costmap = costmap_ros->getCostmap();
    size_x = costmap->getSizeInCellsX();
    size_y = costmap->getSizeInCellsY();

    threshold = .5 * 256; // 50%
  }

  bool RRTPlanner::checkObstacle(double x, double y) {
    unsigned int mx;
    unsigned int my;

    if (costmap->worldToMap(x, y, mx, my)) {
      ROS_INFO("Cost: %.2d", costmap->getCost(mx, my));
      return costmap->getCost(mx, my) > threshold;
    } else {
      ROS_WARN("Goal point outside bounds!!");
      return false;
    }
  }


  bool RRTPlanner::makePlan(const geometry_msgs::PoseStamped& start, const geometry_msgs::PoseStamped& goal,  std::vector<geometry_msgs::PoseStamped>& plan ){
    double start_point[2] = {start.pose.position.x, start.pose.position.y};
    double goal_point[2] = {goal.pose.position.x, goal.pose.position.y};
    
    ROS_INFO("Got a start: %.2f, %.2f, and a goal: %.2f, %.2f", start.pose.position.x, start.pose.position.y, goal.pose.position.x, goal.pose.position.y);

    bool goal_obstacle = checkObstacle(goal_point[0], goal_point[1]);
    ROS_INFO("The goal is an obstacle?: %d", goal_obstacle);

    return true;
  }
};
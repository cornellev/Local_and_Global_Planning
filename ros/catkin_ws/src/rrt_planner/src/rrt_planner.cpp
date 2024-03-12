#include <pluginlib/class_list_macros.h>
#include "rrt_planner/rrt_planner.h"

//register this planner as a BaseGlobalPlanner plugin
PLUGINLIB_EXPORT_CLASS(rrt_planner::RRTPlanner, nav_core::BaseGlobalPlanner)

using namespace std;

//Default Constructor
namespace rrt_planner {

  RRTPlanner::RRTPlanner (){}

  RRTPlanner::RRTPlanner(std::string name, costmap_2d::Costmap2DROS* costmap_ros){
    initialize(name, costmap_ros);
  }

  void RRTPlanner::initialize(std::string name, costmap_2d::Costmap2DROS* costmap_ros){}

  bool RRTPlanner::makePlan(const geometry_msgs::PoseStamped& start, const geometry_msgs::PoseStamped& goal,  std::vector<geometry_msgs::PoseStamped>& plan ){
    return true;
  }
};
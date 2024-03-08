roscore &

rosparam set /test_optim_node/enable_homotopy_class_planning True # Set false to compute one path, True computes multiple
roslaunch teb_local_planner test_optim_node.launch

rosrun planning_sim teb_vel_plot.py # Plot Vel
rosrun rqt_reconfigure rqt_reconfigure # Configuration

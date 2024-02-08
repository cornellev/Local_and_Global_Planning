# Install script for directory: /home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/msg" TYPE FILE FILES
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/DetectedPerson.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/DetectedPersons.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/CompositeDetectedPerson.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/CompositeDetectedPersons.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/TrackedPerson.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/TrackedPersons.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/TrackedPerson2d.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/TrackedPersons2d.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/TrackedGroup.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/TrackedGroups.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/ImmDebugInfo.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/ImmDebugInfos.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/msg/TrackingTimingMetrics.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/srv" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/srv/GetPersonTrajectories.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/cmake" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/include/spencer_tracking_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/share/roseus/ros/spencer_tracking_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/share/common-lisp/ros/spencer_tracking_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/share/gennodejs/ros/spencer_tracking_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/lib/python3/dist-packages/spencer_tracking_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/lib/python3/dist-packages/spencer_tracking_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/cmake" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs/cmake" TYPE FILE FILES
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgsConfig.cmake"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/catkin_generated/installspace/spencer_tracking_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_tracking_msgs" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_tracking_msgs/package.xml")
endif()


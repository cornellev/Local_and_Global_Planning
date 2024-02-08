# Install script for directory: /home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_social_relation_msgs/msg" TYPE FILE FILES
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/msg/SocialRelation.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/msg/SocialRelations.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/msg/SocialActivity.msg"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/msg/SocialActivities.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_social_relation_msgs/cmake" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/catkin_generated/installspace/spencer_social_relation_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/include/spencer_social_relation_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/share/roseus/ros/spencer_social_relation_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/share/common-lisp/ros/spencer_social_relation_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/share/gennodejs/ros/spencer_social_relation_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/lib/python3/dist-packages/spencer_social_relation_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/devel/lib/python3/dist-packages/spencer_social_relation_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/catkin_generated/installspace/spencer_social_relation_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_social_relation_msgs/cmake" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/catkin_generated/installspace/spencer_social_relation_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_social_relation_msgs/cmake" TYPE FILE FILES
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/catkin_generated/installspace/spencer_social_relation_msgsConfig.cmake"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/catkin_generated/installspace/spencer_social_relation_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/spencer_social_relation_msgs" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/rviz_plugins/spencer_messages/spencer_social_relation_msgs/package.xml")
endif()


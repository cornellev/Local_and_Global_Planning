# Install script for directory: /home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/dynamic_xml_config

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/dynamic_xml_config/catkin_generated/installspace/dynamic_xml_config.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_xml_config/cmake" TYPE FILE FILES
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/dynamic_xml_config/catkin_generated/installspace/dynamic_xml_configConfig.cmake"
    "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/dynamic_xml_config/catkin_generated/installspace/dynamic_xml_configConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/dynamic_xml_config" TYPE FILE FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/src/external/ros_motion_planning/src/third_party/dynamic_xml_config/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/dynamic_xml_config" TYPE PROGRAM FILES "/home/sloth/Local_and_Global_Planning/ros/catkin_ws/build/external/ros_motion_planning/src/third_party/dynamic_xml_config/catkin_generated/installspace/obstacles_generate_ros.py")
endif()


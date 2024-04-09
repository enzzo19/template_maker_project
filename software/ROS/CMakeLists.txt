cmake_minimum_required(VERSION 2.8.3)
project(my_ros_package)

# Set the minimum required version of CMake.
# This ensures that the CMake version used meets the requirements for the ROS version being used.

## Find catkin macros and libraries.
## The `catkin` package is required for building ROS packages.
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

# Declare the catkin package.
## This command must be included at the beginning of the CMakeLists.txt file for a ROS package.
## It defines the package and specifies its dependencies.
catkin_package(
  CATKIN_DEPENDS roscpp std_msgs
)

# Specify locations of header files.
## This command tells the compiler where to find header files.
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

# Declare a C++ executable.
## This command specifies a C++ executable to be built from the source files.
add_executable(my_node src/my_node.cpp)

# Link the executable with the necessary libraries.
## This command specifies the libraries to link with the executable.
target_link_libraries(my_node
  ${catkin_LIBRARIES}
)

# Install rules.
## These commands specify files to be installed when the package is installed.
install(TARGETS my_node
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

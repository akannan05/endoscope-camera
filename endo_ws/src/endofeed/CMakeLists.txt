cmake_minimum_required(VERSION 3.8)
project(endofeed)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(image_transport REQUIRED)
find_package(OpenCV REQUIRED COMPONENTS highgui videoio)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(include)

add_executable(publisher_endo_cam src/publisher_endo_cam.cpp)
target_link_libraries(publisher_endo_cam
    cv_bridge::cv_bridge
    image_transport::image_transport
    opencv_highgui
    opencv_videoio
    rclcpp::rclcpp
    "${sensor_msgs_TARGETS}"
    "${std_msgs_TARGETS}"
)

install(
    TARGETS publisher_endo_cam
    RUNTIME DESTINATION lib/${PROJECT_NAME}
)

install(
    DIRECTORY include/
    DESTINATION include/${PROJECT_NAME}
)

ament_export_include_directories(include)
ament_export_dependencies(cv_bridge image_transport rclcpp sensor_msgs std_msgs)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

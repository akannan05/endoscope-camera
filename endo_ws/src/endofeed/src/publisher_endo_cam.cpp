#include <sstream>

#include "cv_bridge/cv_bridge.hpp"
#include "image_transport/image_transport.hpp"
#include "opencv2/core/mat.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/videoio.hpp"
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/header.hpp"

int main(int argc, char ** argv){
    if(argv[1] == NULL)
        return 1;

    rclcpp::init(argc, argv);
    rclcpp::NodeOptions options;
    rclcpp::Node::SharedPtr node = rclcpp::Node::make_shared("endo_pub", options);
    image_transport::ImageTransport it(node);
    image_transport::Publisher pub = it.advertise("endocam/feed", 1);

    std::istringstream video_sourceCmd(argv[1]);
    int video_source;

    if(!(video_sourceCmd >> video_source))
        return 1;

    cv::VideoCapture cap(video_source);

    if(!cap.isOpened())
        return 1;

    cv::Mat frame, resized_frame;
    std_msgs::msg::Header hdr;
    sensor_msgs::msg::Image::SharedPtr msg;

    int new_width = 640;
    int new_height = 640; //resize image 

    rclcpp::WallRate loop_rate(20);
    while(rclcpp::ok()){
        cap >> frame;

        if(!frame.empty()){
            cv::resize(frame, resized_frame, cv::Size(new_width, new_height));
            msg = cv_bridge::CvImage(hdr, "bgr8", resized_frame).toImageMsg();
            pub.publish(msg);
            cv::waitKey(1);
        }

        rclcpp::spin_some(node);
        loop_rate.sleep();
    }

    return 0;
}

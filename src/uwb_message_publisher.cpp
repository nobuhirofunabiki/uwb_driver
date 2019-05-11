#include <ros/ros.h>

int main(int argc, char **argv){
    ros::init(argc, argv, "uwb_message_publisher");
    ros::NodeHandle nh;
    ros::NodeHandle nh_private("~");

    if (!nh_.private.getParam("comm_port", comm_port_)){
        ROS_WARN("Port is not defined.");
    }
    if (!nh_private.getParam("rate", rate_)){
        ROS_WARN("Rate is not defined.");
    }

    ros::Publisher uwb_message_pub = nh_private.advertise<uwb_msgs::Anchor>("uwb_signal", 10);

    while(ros::ok()){
        
    }
}
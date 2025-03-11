import time
import rclpy

from sensor_msgs.msg import Image
from std_msgs.msg import String
from rclpy.qos import qos_profile_sensor_data

from ultralytics import YOLO

def main():
    rclpy.init()

    node = rclpy.create_node('detector')

    detection_model = YOLO("./models/best.pt")

    pub = node.create_publisher(String, "detector/detect_classes", 5)

    def callback(data):
        array = rosnumpy.numpify(data)
        if pub.get_subscription_count() > 0:  # Correct way to check for subscribers
            det_result = detection_model(array)
            classes = det_result[0].boxes.cls.cpu().numpy().astype(int)
            names = [det_result[0].names[i] for i in classes]

            msg = String()
            msg.data = str(names)
            pub.publish(msg)

    sub = node.create_subscription(Image, "endocam/feed", callback, qos_profile_sensor_data)

    rclpy.spin(node)  # Correct way to keep node alive

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


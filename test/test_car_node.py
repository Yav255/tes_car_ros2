import time
import rclpy
from geometry_msgs.msg import Twist


def test_car_speed():
    rclpy.init()

    test_node = rclpy.create_node('test_qa_node')

    mock_pub = test_node.create_publisher(Twist,'/cmd_vel', 10)

    recieved_messages = []

    def test_callback(msg):
        recieved_messages.append(msg)

    test_node.create_subscription(Twist,'/cmd_vel', test_callback,10)

    fake_msg = Twist()
    fake_msg.linear.x =1.0

    mock_pub.publish(fake_msg)

    rclpy.spin_once(test_node,timeout_sec=1)

    test_node.destroy_node()
    rclpy.shutdown()

   

    assert len(recieved_messages) >0 

    assert recieved_messages[0].linear.x ==1.0

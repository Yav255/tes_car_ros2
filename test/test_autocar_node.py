import pytest
import time 
import rclpy
from geometry_msgs.msg import Twist

@pytest.fixture(scope = "function")
def ros_context():
    rclpy.init()
    yield 
    if rclpy.ok():
        rclpy.shutdown()

@pytest.mark.parametrize("input_speed, expected_speed" , 
[ (1.0,1.0) ,(-0.5,-.5), (0.0 , 0.0)])
def test_sensor_speed(ros_context,input_speed,expected_speed):
    test_node  = rclpy.create_node("qa_matrix_test")

    mock_publish = test_node.create_publisher(Twist,"/cmd_vel" ,10)
    received_msgs = []

    def test_callback(msg):
        received_msgs.append(msg)

    test_node.create_subscription(Twist,"/cmd_vel" , test_callback , 10)

    fake_msg = Twist()
    fake_msg.linear.x = input_speed
    mock_publish.publish(fake_msg)

    timeout = time.time()+ 1.0

    while len(received_msgs) == 0 and time.time() < timeout:
        rclpy.spin_once(test_node,timeout_sec=0.1)

    test_node.destroy_node()

    assert len(received_msgs)> 0 , f"Input speed: {input_speed}"
    assert received_msgs[0].linear.x == expected_speed, \
         f"Data corruption! Sent {input_speed}, but int excepted {received_msgs[0].linear.x}"
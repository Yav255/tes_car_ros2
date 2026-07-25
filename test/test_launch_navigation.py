import pytest
import unittest
import launch
import launch_ros.actions
import launch_testing.actions
import time
import rclpy
from std_msgs.msg import String

@pytest.mark.launch_test
def generate_test_description():

    talker_node = launch_ros.actions.Node(package= "demo_nodes_cpp",
    executable='talker',
    name = 'test_talker')

    return launch.LaunchDescription([ talker_node ,
    launch_testing.actions.ReadyToTest()])

class Test_talker_Integ(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        rclpy.init()
    
    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self.node = rclpy.create_node("test_talker_listener")

    def tearDown(self):
       self.node.destroy_node()

    def test_received_msg(self):
        received_messages = []

        def msg_callback(msg):
            received_messages.append(msg.data)

        self.node.create_subscription(String, "/chatter", msg_callback,10)

        start_time = time.time()
        while time.time() - start_time < 15.0:
            rclpy.spin_once(self.node, timeout_sec=0.5)
            if len(received_messages) >0:
                break
        

        self.assertGreater(len(received_messages),0 ,"No messages recieved on /chatter ")
        self.assertIn("Hello World", received_messages[0])




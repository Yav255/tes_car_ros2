import rclpy
import unittest
from my_testingpkg.carNode import AutonomousCarNode
from geometry_msgs.msg import Twist

class TestCarNode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rclpy.init()
        
    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()
    
    def test_speed_is_one(self):
        node = AutonomousCarNode()
        received_messages = []
        def cb(msg):
            received_messages.append(msg)
        
        test_sub = node.create_subscription(Twist, '/cmd_vel', cb , 10)

        for _ in range(15):
            rclpy.spin_once(node , timeout_sec=0.1)
        
        node.destroy_subscription(test_sub)
        node.destroy_node()


        self.assertTrue(len(received_messages) >0 ,'No messages were published!')

        last_msg = received_messages[-1]
        self.assertEqual(last_msg.linear.x, 1.0 ,f"Expected speed 1.0 but got {last_msg.linear.x}")

if __name__ == '__main__':
    unittest.main()

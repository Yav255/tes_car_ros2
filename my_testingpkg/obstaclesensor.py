import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ObstacleSensorNode(Node):

    def __init__(self):
        super().__init__("obstacle_sensor_node")

        self.subscriber_ = self.create_subscription(Twist,'/cmd_vel',self.sub_callback,10)
        self.subscriber_

    def sub_callback(self,msg):
        current_speed = msg.linear.x
        self.get_logger().info(f'📢 Sensor intercepted Car Speed: {current_speed} m/s')


def main(args = None):
        rclpy.init(args = args)
        node = ObstacleSensorNode()

        try:
            rclpy.spin(node)
        except KeyboardInterrupt:
            pass
        node.destroy_node()
        rclpy.shutdown()

if __name__ =='__main__':
        main()
import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist


class TurtleController(Node):

    def __init__(self):
        super( ).__init__("turtle_controller")

        self.publisher = self.create_publisher(Twist , "/turtle1/cmd_vel" , 10)

        self.timer = self.create_timer(0.5 , self.control_cb)

    def  control_cb(self):
            msg  = Twist()
            msg.linear.x = 1.0
            msg.angular.z = 0.5
            self.publisher.publish(msg)

def main(args =None):
    rclpy.init(args = args)
    node  = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

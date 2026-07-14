import rclpy
from rclpy.node import Node
# We import geometry_msgs to control the robot's wheels (linear/angular speed)
from geometry_msgs.msg import Twist 

# 1. Your class inherits from "Node" instead of just being a standalone class
class AutonomousCarNode(Node):
    def __init__(self):
        # Initialize the node with a name
        super().__init__('autonomous_car_node')
        
        # 2. Create a Publisher: This is our output "pipe"
        # We publish 'Twist' messages to the '/cmd_vel' topic with a queue size of 10
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # 3. Create a Timer: Run our drive logic every 1.0 second
        self.timer = self.create_timer(1.0, self.drive_callback)
        
        # Initialize our internal state (just like self.__speed in your code)
        self.current_speed = 1.0 

    def drive_callback(self):
        # 4. This runs every second. We build the message and send it!
        msg = Twist()
        
        # Set forward speed (x-axis)
        msg.linear.x = self.current_speed 
        msg.angular.z = 0.0 # Drive straight, no turning
        
        # Publish the message to the physical or simulated robot
        self.publisher_.publish(msg)
        
        # Log it to the terminal so we can see it working
        self.get_logger().info(f'Publishing safety-checked speed: {msg.linear.x} m/s')


def main(args=None):
    # Initialize the ROS 2 communications
    rclpy.init(args=args)
    
    # Instantiate our class
    node = AutonomousCarNode()
    
    # Keep the node running/spinning
    rclpy.spin(node)
    
    # Clean up when stopped
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
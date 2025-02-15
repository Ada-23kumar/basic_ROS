import rclpy
import rclpy.destroyable
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listiner_callback,
            10
        )

    def listiner_callback(self, msg):
        self.get_logger().info(f"recived {msg.data}")

def main(args = None):
    rclpy.init(args = args)

    #create Node
    listnerNode = ListenerNode()

    # use Node
    rclpy.spin(listnerNode)

    # destroy Node
    listnerNode.destroy_node()


    # shutdown
    rclpy.shutdown()

if __name__ == "__main__":
    main()
import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        Node(package='harinetra_bringup', executable='sensor_node', name='sensor_node'),
        Node(package='harinetra_bringup', executable='ai_node', name='ai_node'),
        Node(package='harinetra_bringup', executable='ui_node', name='ui_node'),
    ])

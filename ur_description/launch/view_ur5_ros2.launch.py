import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # URDF file to be loaded by Robot State Publisher
    urdf = os.path.join(
        get_package_share_directory('ur_description'), 
            'urdf', 'ur5_robot' + '.urdf'
    )

    # .rviz file to be loaded by rviz2
    rviz = os.path.join(
        get_package_share_directory('ur_description'), 
            'cfg', 'view_robot.rviz'
    )
    
    # Set LOG format
    os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '{time}: [{name}] [{severity}] - {message}'

    return LaunchDescription( [
        # Robot State Publisher
        Node(package='robot_state_publisher', node_executable='robot_state_publisher',
             output='screen', arguments=[urdf]),

        # Rviz2
        Node(package='rviz2', node_executable='rviz2',
             output='screen', arguments=['-d', rviz]),
    ])

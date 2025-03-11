from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node  

def generate_launch_description():
    parameters=[]
    arguments=[
        '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
        '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
        '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
        '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
        '/scan/points@sensor_msgs/msg/PointCloud2@gz.msgs.PointCloudPacked',
        '/imu@sensor_msgs/msg/Imu[gz.msgs.IMU',
        '/scan/points@gz.msgs.PointCloud[sensor_msgs/msg/PointCloud2]',
        '/body_camera/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo',
        '/body_camera/image@sensor_msgs/msg/Image[gz.msgs.Image',
        '/leo/realsense_d455/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo',
        '/leo/realsense_d455/image@sensor_msgs/msg/Image[gz.msgs.Image',
        '/leo/realsense_d455/depth_image@sensor_msgs/msg/Image[gz.msgs.Image',
        '/gps/fix@sensor_msgs/msg/NavSatFix[ignition.msgs.NavSat',
        '/world/default/model/leorover/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model',
        '/odom/tf@tf2_msgs/msg/TFMessage[ignition.msgs.Pose_V',

    ]

    remappings=[
        ("/odom/tf", "tf"),
        ('/cmd_vel', '/cmd_vel'),
        ('/imu', '/imu'),
        ('/body_camera/camera_info', '/leo/body_camera/camera_info'),
        ('/body_camera/image', '/leo/body_camera/image'),
        ('/leo/realsense_d455/camera_info', '/leo/realsense_d455/camera_info'),
        ('/leo/realsense_d455/image', '/leo/realsense_d455/image'),
        ('/leo/realsense_d455/depth_image', '/leo/realsense_d455/depth_image'),
        ('/world/default/model/leorover/joint_state','/joint_states')
    ]

    return LaunchDescription([

    # Nodes to launch
    Node(
        package='ros_gz_bridge', 
        executable='parameter_bridge', 
        output='screen',
        arguments=arguments,
        remappings=remappings),
    ])

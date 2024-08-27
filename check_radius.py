#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from std_msgs.msg import Bool

turtle_poses = {}

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def check_proximity():
    global within_range_publisher 

    if 'turtle1' in turtle_poses and 'turtle2' in turtle_poses:
        turtle1_pose = turtle_poses['turtle1']
        turtle2_pose = turtle_poses['turtle2']
        radius = 3.0
        dist = distance(turtle1_pose.x, turtle1_pose.y, turtle2_pose.x, turtle2_pose.y)
        within_range = dist < radius
        within_range_publisher.publish(within_range)

def updating_pose(data, turtle_name):
    global turtle_poses  # Access the global turtle_poses dictionary

    turtle_poses[turtle_name] = data
    check_proximity()

def main():
    global within_range_publisher

    rospy.init_node('check_radius')
    within_range_publisher = rospy.Publisher('within_range', Bool, queue_size=10)

    rospy.Subscriber('/turtle1/pose', Pose, updating_pose, 'turtle1')
    rospy.Subscriber('/turtle2/pose', Pose, updating_pose, 'turtle2')

    rospy.spin()

if __name__ == '__main__':
    main()

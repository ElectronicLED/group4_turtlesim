#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def callback(data):
      rospy.loginfo(data.data)


def main():
    rospy.init_node("Health_node")
    sub = rospy.Subscriber("turtle1_attack" , String , callback)

    rospy.spin()


if __name__ == '__main__':
        main()
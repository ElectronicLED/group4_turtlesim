#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8

def callback(data):
     rospy.loginfo(data.data)
     
     


def main():
    sub = rospy.Subscriber('attack_count', Int8, callback)
    rospy.init_node('gameEngineNode')
    rospy.spin()
    


if __name__ == '__main__':
    main()
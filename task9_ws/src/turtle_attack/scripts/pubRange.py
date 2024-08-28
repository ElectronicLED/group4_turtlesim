#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool



def main():
    pub = rospy.Publisher('withinRange', Bool, queue_size=10)
    rospy.init_node('check_radius')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(True)
        pub.publish(True)
        rate.sleep()


if __name__ == '__main__':
        main()
 
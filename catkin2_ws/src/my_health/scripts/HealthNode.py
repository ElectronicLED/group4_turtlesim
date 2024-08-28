#!/usr/bin/env python
# Software License Agreement (BSD License)


import rospy
from std_msgs.msg import String

health = 100
def callback(data):
    global health
    rospy.loginfo('I am under %s', data.data)
    health=health-50
    rospy.loginfo('current health = %i', health)

def HealthNode():

    
    rospy.init_node('HealthNode', anonymous=True)

    rospy.Subscriber('turtle2_attack', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    HealthNode()

#!/usr/bin/env python
# Software License Agreement (BSD License)


import rospy
from std_msgs.msg import String

def attacker():
    pub = rospy.Publisher('turtle2_attack', String, queue_size=10)
    rospy.init_node('attacker', anonymous=True)
    rate = rospy.Rate(0.1) # 10hz
    while not rospy.is_shutdown():
        attack_str = "attack %s" % rospy.get_time()
        rospy.loginfo(attack_str)
        pub.publish(attack_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        attacker()
    except rospy.ROSInterruptException:
        pass

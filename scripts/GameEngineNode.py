#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

##VI note : All msg names and Topic names should be changed with those you've used while creating your nodes/topics that's used in this code


def Gamestats (msg):
    rospy.loginfo("turtle1Health=,(" + str(msg.turtle1_Health) + ")")
    rospy.loginfo("turtle2Health=,(" + str(msg.turtle2_Health) + ")")
    rospy.loginfo("turtle1AttacksRemaining=,(" + str(msg.turtle1_attacks) + ")")
    rospy.loginfo("turtle2AttacksRemaining=,(" + str(msg.turtle2_attacks) + ")")

def GameOver(msg):
    while not rospy.is_shutdown():
        if int(msg.turtle1_attacks) == 0 :
            if int(msg.turtle2_Health)>int(msg.turtle1_Health):
                rospy.loginfo("Turtle 2 Wins With,(" + str(msg.turtle2_Health) + ")HP")
                quit_pub.publish("shutdown")
        elif int(msg.turtle2_attacks) == 0 :
             if int(msg.turtle1_Health)>int(msg.turtle2_Health):
                rospy.loginfo("Turtle 1 Wins With,(" + str(msg.turtle1_Health) + ")HP")
                quit_pub.publish("shutdown")   
        else :
            continue                     



if __name__ == '__main__':
    
    rospy.init_node('game_engine_node')
    sub1=rospy.Subscriber("/turtle1/Health",callback=Gamestats&GameOver)
    sub2=rospy.Subscriber("/turtle2/Health",callback=Gamestats&GameOver)
    sub3=rospy.Subscriber("/attack_count",callback=Gamestats&GameOver)
    quit_pub = rospy.Publisher("turtlesim/shutdown", String, latch=True)

    rospy.spin()
    

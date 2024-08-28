#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
from std_msgs.msg import Bool
import pynput.keyboard as kb

global checkRange
global counter
counter = 0

#function to recieve the boolen value 
def callback(data):
    global checkRange
    checkRange = data.data



#function to check if key 'q' is pressed
def on_press(key):
        global checkRange
        global counter
        if checkRange:
            if key.char == 'q':
               pub_attack.publish("attack")
               counter += 1
               pub_count.publish(counter)
        else:
            if key.char =='q':
                rospy.loginfo("Out of Range")



def main():
    global pub_attack
    global pub_count
    rospy.init_node("Attack") #initialize the node

    rospy.loginfo("START")
    #make the publishers and the subscriber
    pub_attack = rospy.Publisher("turtle1_attack" , String , queue_size=10)
    pub_count = rospy.Publisher("attack_count" ,Int8 , queue_size=10)
    sub = rospy.Subscriber("withinRange" , Bool , callback)

    # listener for key event
    with kb.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    while not rospy.is_shutdown():
        try:
            main()
        except rospy.ROSInterruptException:
            pass
        except AttributeError:
            pass
        rospy.sleep(10)



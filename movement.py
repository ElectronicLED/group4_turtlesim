#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard

key_states = {'w': False, 's': False, 'a': False, 'd': False}
twist = Twist()  # Initialize the Twist message outside of functions

def update_twist():
    global twist
    twist.linear.x = 0
    twist.linear.y = 0
    twist.angular.z = 0

    if key_states['w'] and key_states['a']:
        twist.angular.z = 2.0  # Rotate left while moving forward
        return
    if key_states['w'] and key_states['d']:
        twist.angular.z = -2.0  # Rotate right while moving forward
        return

    if key_states['w']:
        twist.linear.x = 2.0  # Move forward
    if key_states['s']:
        twist.linear.x = -2.0  # Move backward

    if key_states['a']:
        twist.linear.y = 2.0  # Move left
    if key_states['d']:
        twist.linear.y = -2.0  # Move right


def on_press(key):
    try:
        key_char = key.char
        if key_char in key_states:
            key_states[key_char] = True
            update_twist()
            pub.publish(twist)
    except AttributeError:
        pass

def on_release(key):
    global key_states  # Declare key_states as global to avoid UnboundLocalError
    try:
        key_char = key.char
        if key_char in key_states:
            key_states[key_char] = False
            update_twist()
            pub.publish(twist)
    except AttributeError:
        pass

    if key == keyboard.Key.esc:
        # Stop listener
        return False


def publish_action():
    global pub
    rospy.init_node('turtle_controller_node', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.loginfo("Turtle action publisher is ready. Use W, A, S, D to move.")

    # Start listening for keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    try:
        publish_action()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        pass

    

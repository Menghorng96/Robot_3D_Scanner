#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import time


if __name__ == "__main__":

     rospy.init_node("turnTable", anonymous=True)
     turnTable = rospy.Publisher('/turn_table/turn_table/joint_position_controller/command',Float64, queue_size=1.0) 

     while not rospy.is_shutdown():
        try:
           r = input("from -3.14 to 3.14: ")
           turnTable.publish(r)
           #time.sleep(3)
        except KeyboardInterrupt: 
            print "Ctrl+c"
            break

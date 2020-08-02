#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

if __name__ == "__main__":
     rospy.init_node("test", anonymous=True)
     publisher = rospy.Publisher('/turn_table/joint_position_controller/command',Float64, queue_size=1.0)
     while not rospy.is_shutdown():
        try:
            position = input("Please input postion between -180 ot 180 degree: ")
            publisher.publish(float(position)*3.14/180)
        except KeyboardInterrupt: 
            print "Ctrl+c"
            break

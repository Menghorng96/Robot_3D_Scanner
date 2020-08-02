#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import time

def position_sawyer (j0, j1, j2, j3, j4, j5, j6):
     sawyer_j0.publish(j0)
     sawyer_j1.publish(j1)
     sawyer_j2.publish(j2)
     sawyer_j3.publish(j3)
     sawyer_j4.publish(j4)
     sawyer_j5.publish(j5)
     sawyer_j6.publish(j6)

if __name__ == "__main__":

     rospy.init_node("example", anonymous=True)
     sawyer_h = rospy.Publisher('/sawyer/sawyer/head_pan_position_controller/command',Float64, queue_size=1.0)
     sawyer_j0 = rospy.Publisher('/sawyer/sawyer/right_j0_position_controller/command',Float64, queue_size=1.0)
     sawyer_j1 = rospy.Publisher('/sawyer/sawyer/right_j1_position_controller/command',Float64, queue_size=1.0)
     sawyer_j2 = rospy.Publisher('/sawyer/sawyer/right_j2_position_controller/command',Float64, queue_size=1.0)
     sawyer_j3 = rospy.Publisher('/sawyer/sawyer/right_j3_position_controller/command',Float64, queue_size=1.0)
     sawyer_j4 = rospy.Publisher('/sawyer/sawyer/right_j4_position_controller/command',Float64, queue_size=1.0)
     sawyer_j5 = rospy.Publisher('/sawyer/sawyer/right_j5_position_controller/command',Float64, queue_size=1.0)
     sawyer_j6 = rospy.Publisher('/sawyer/sawyer/right_j6_position_controller/command',Float64, queue_size=1.0)
     turnTable = rospy.Publisher('/turn_table/turn_table/joint_position_controller/command',Float64, queue_size=1.0) 

     while not rospy.is_shutdown():
        try:
           #neutral: [0.00, -1.18, 0.00, 2.18, 0.00, 0.57, 3.3161]
           #shipping: [0.00, -1.57, 0.00, 2.79, 0.00, -2.79, 3.3161]
           position_sawyer(0.00, -1.18, 0.00, 2.7, 1.5, 0.0, 3.4)
           #turnTable.publish(3.0)  
           #time.sleep(3)
           #position_sawyer(0.1, -1.57, 0.00, 2.79, 0.00, -2.79, 3.3161)
           #turnTable.publish(-3.0)
           #time.sleep(3)
        except KeyboardInterrupt: 
            print "Ctrl+c"
            break

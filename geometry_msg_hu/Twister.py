#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

temp = rospy.Publisher('chatter', Twist)
print(temp)
temp.linear.x = 0
temp.linear.y = 0
temp.linear.z = 0
"""
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
"""

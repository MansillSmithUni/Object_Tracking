#!/usr/bin/env python3
import rospy
import roslib
import message_filters
import time
from features_msgs.msg import FeatureMasks
# from sensor_msgs.msg import Image

class ObjectTrackingNode:
    def __init__ (self, subscribeTopics):        
        self.subscibed = []
        for i in subscribeTopics:
            subscribed = message_filters.Subscriber(i, FeatureMasks, callback=self.callback)
            self.subscibed.append(subscribed)
        

        self.ts = message_filters.ApproximateTimeSynchronizer([sub for sub in self.subscibed], 1, 1) 
        self.ts.registerCallback(self.callback)

    def callback(self, *args):
        print("Callback")


def getArgs():
    myargs = {}

    myargs['subscribe_topics'] = rospy.get_param('~subscribe_topics')

    return myargs

def main():
    rospy.init_node("apple_fruitlet_object_tracking", anonymous=False)
    myargs = getArgs()

    obn = ObjectTrackingNode(myargs['subscribe_topics'])

    while not rospy.is_shutdown():
        time.sleep(1)

if __name__ == "__main__":
    main()
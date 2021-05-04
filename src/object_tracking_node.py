#!/usr/bin/env python3
import rospy
import message_filters
import time
from features_msgs.msg import FeatureMasks
from sensor_msgs.msg import Image

class ObjectTrackingNode:
    def __init__ (self, subscribeTopics):
        rospy.init_node("/apple_fruitlet_object_tracking", anonymous=False)
        
        self.subscibed = []
        for i in subscribeTopics:
            subscribed = message_filters.Subscriber(i, Image, callback=self.callback)
            self.subscibed.append(subscribed)
        

        self.ts = message_filters.ApproximateTimeSynchronizer(self.subscibed, 1, 1) 
        self.ts.registerCallback(self.callback)

    def callback(self, *args):
        print("Callback")


def main():
    obn = ObjectTrackingNode("/camera/color/image_raw/")

    while not rospy.is_shutdown():
        time.sleep(1)

if __name__ == "__main__":
    main()
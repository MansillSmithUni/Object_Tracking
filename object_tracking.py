import rospy
import message_filters
import time
from features_msgs.msg import FeatureMasks
from sensor_msgs.msg import Image

class ObjectTrackingNode:
    def __init__ (self, features_topics):

        # sub_features = []
        # for i in range(len(features_topics)):
        #     sub_feature = message_filters.Subscriber(features_topics[i], FeatureMasks, callback=self.callback)
        #     sub_features.append(sub_feature)

        sub_features = []
        sub_features.append(message_filters.Subscriber("/camera/color/image_raw", Image, callback=self.callback))

        self.ts = message_filters.ApproximateTimeSynchronizer([sub for sub in sub_features], 1, 1) 
        self.ts.registerCallback(self.callback)

    def callback(self, *args):
        print("Callbacl")
        feature_msg = list(args)
        for i, feature in enumerate(feature_msg):
            print(feature)

def main():
    obn = ObjectTrackingNode(["/features"])

    while not rospy.is_shutdown():
        time.sleep(0.5)

if __name__ == "__main__":
    main()
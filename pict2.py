#!/usr/bin/env python
import cv2
import rospy
import time
from sensor_msgs.msg import Image

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

rospy.init_node('topic_publisher')
pub = rospy.Publisher('imgs', Image)
rate = rospy.Rate(.05)
img_counter = 0

while not rospy.is_shutdown():
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    img_name = "[FOLDER ADDRESS HERE]\opencv_frame_{}.jpg".format(img_counter)
    cv2.imwrite(img_name, frame)
    pub.publish(frame)
    img_counter += 1
    '''
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    '''
    rate.sleep(.05)

cam.release()

cv2.destroyAllWindows()

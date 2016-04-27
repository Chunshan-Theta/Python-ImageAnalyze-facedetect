# Program Name: facedetect.py
# Author: skynet
# Date: 2015/9
#
import cv2 
import sys 
 
image_file = "picture.jpg"
args = sys.argv
if len(args)>=2:
    image_file = args[1]
 
casc_path = "./xml/haarcascade_frontalface_default.xml"
 
faceCascade = cv2.CascadeClassifier(casc_path)
image = cv2.imread(image_file)
 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)
print "Found {0} faces!".format(len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w, y+h),(128,255,0),2)
cv2.namedWindow('found', cv2.WINDOW_NORMAL)
cv2.imshow("found", image)
cv2.waitKey(0)
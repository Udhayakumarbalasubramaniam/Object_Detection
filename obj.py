import imutils
import cv2
"""img=cv2.imread('new.jfif')

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#dst=cv2.threshold(src,threshold,maxValueForThreshold,binary,type)[1]
thresholding=cv2.threshold(grayimg,170,255,cv2.THRESH_BINARY)[1]
cv2.imshow("new.jfif",thresholding)

resizedImg=imutils.resize(img,width=100)
"""
"""*******************This part is for the resizing the image ************************


########cv2.imshow('n.jpg',img)
##cv2.imshow('Resized.jpg',resizedImg)

##gausianImg=cv2.GaussianBlur(src,(kernel),boardType

gaussianImg=cv2.GaussianBlur(img,(41,41),50)
gaussianImg1=cv2.GaussianBlur(img,(21,21),0)

cv2.imshow("Original",img)
cv2.imshow("Gaussianblur",gaussianImg)
cv2.imshow("GaussiamBlur",gaussianImg1)"""

##vs=cv2.VideoCapture(0)
###Here the VideoCapture(0) denotes to use the main camera in the laptop, 1 to externel camera etc.
##
##
##while True:
##    _,img=vs.read()
###here the underscore is used to get the frame.
###initially vs returns 2 values. 1 is detect the camera, and another one for returning the frames captured.
##    
##    cv2.imshow("VideoStream",img)
##
##    key=cv2.waitKey(1)
##
##    print(key)
##    if key==ord("q"):
##        break
##vs.release()
##cv2.destroyAllWindows()

import imutils
import cv2

cam = cv2.VideoCapture(0)

first_frame = None
area = 500

while True:
    _, img = cam.read()
    text = "Normal"

    img = imutils.resize(img, width=1000)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussian_img = cv2.GaussianBlur(gray_img, (21, 21), 0)

    if first_frame is None:
        first_frame = gaussian_img
        continue

    img_diff = cv2.absdiff(first_frame, gaussian_img)
    thresh_img = cv2.threshold(img_diff, 25, 255, cv2.THRESH_BINARY)[1]
    thresh_img = cv2.dilate(thresh_img, None, iterations=2)
    cnts = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        text = "Moving Object Detected"
    print(text)
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("camerafeed", img)

    key = cv2.waitKey(10)
    print(key)
    if key == 113:  # 113 corresponds to the 'q' key
        break

cam.release()
cv2.destroyAllWindows()

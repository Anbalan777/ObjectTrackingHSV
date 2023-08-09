import cv2
import imutils 
vs=cv2.VideoCapture("M:\Download\Connect Two PC Using Ethernet or WiFi _ Transfer Files Over Network at 1Gbps _ Faster Than SSD_HDD.mp4")
uppervalue=(15,161,188) 
lowervalue=(60,255,255)

while True:
    _,img=vs.read()
    img=imutils.resize(img,width=920)
    blur=cv2.GaussianBlur(img,(21,21),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,uppervalue,lowervalue)
    mask=cv2.dilate(mask,None,iterations=2)
    mask=cv2.erode(mask,None,iterations=2)
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len (cnts) > 0:
        c=max((cnts),key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        if radius > 10:
            cv2.circle(img,(int(x),int(y)),int(radius),(0,255,105),2)
            cv2.circle(img,center,5,(255,0,255),-2)
    cv2.imshow("VideoStream",img)
    if cv2.waitKey(1) &0xFF == 27:
        break
vs.release()
cv2.destroyAllWindows()    
# _,img=vs.read() #read camera frames
#     img=imutils.resize(img,width=920) #resize the img
#     blur=cv2.GaussianBlur(img,(21,21),0) #blur the image
#     hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV) # normal to Hsv formate
#     mask=cv2.inRange(hsv,uppervalue,lowervalue) 
#     mask=cv2.erode(mask,None,iterations=2) # apply erodetion and dialtion methode
#     mask=cv2.dilate(mask,None,iterations=2)
#     cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2] # take contours value 

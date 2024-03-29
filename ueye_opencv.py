import cv2

cap = cv2.VideoCapture(1)

#Fast frame rate, low accuracy
tracker = cv2.legacy.TrackerMOSSE_create()
#Slow frame rate, high accuracy
#tracker = cv2.TrackerCSST_create()

success, img = cap.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)



def drawBox(img, bbox):

    # Get coordinates.
    # x is the pixel value corresponding to horizontal movement of the object.
    # (i.e. x = 0 is the far left of the screen, bigger number is further to the right)
    # y is the pixel value corresponding to vertical movement of the object.
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)


while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    print(bbox)
    print(cap)
    success, bbox = tracker.update(img)


    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Lost", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img, str(int(fps)), (75,50), cv2.FONT_HERSHEY_COMPLEX, 0.7,(0,0,255),2)

    cv2.imshow("Tracking",img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
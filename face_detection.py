import cv2
import os
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480) 

if cap.isOpened():
    _,frame = cap.read()
    cap.release() #releasing camera immediately after capturing picture
    if _ and frame is not None:
        cv2.imwrite('img.jpg', frame)
        cv2.destroyAllWindows()

cap.release()
os.system("git add .")
os.system("git commit -m 'update' ")
os.system("git push")



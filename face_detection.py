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
os.system("cd .. ")
os.system("sudo ssh -i latest ubuntu@129.213.50.216")
os.system("cd hackathon/yolo-9000/darknet/Data")
os.system("git pull https://github.com/Tamoghna-Sarkar/vm")
os.system("cd ..")
os.system("python runthis2.py")
os.system("git add .")
os.system("git commit -m "from vm")
os.system("git push")
os.system("exit")
os.system("cd Desktop\vm")
os.system("git pull")
os.system("python texttospeech.py")


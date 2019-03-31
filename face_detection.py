import cv2
from gtts import gTTS 
import os
import time
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480) 

if cap.isOpened():
    _,frame = cap.read()
    cap.release() #releasing camera immediately after capturing picture
    if _ and frame is not None:
        cv2.imshow("window", frame)
        cv2.imwrite('img.jpg', frame)
        cv2.destroyAllWindows()

cap.release()
os.system("git add .")
os.system("git commit -m 'update' ")
os.system("git push")
time.sleep(45)
os.system("git pull")

def texttospeech(filename):
    mytext = 'Welcome to Realtime Image Captionaning cognitive Eyes'
    tfile = open('filename', 'r')
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj = gTTS(text=tfile, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")

textospeech('result.txt')



os.system("python speechtotext.py")


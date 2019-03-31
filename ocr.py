from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from gtts import gTTS 
import cv2
import os 
path = 'image.png'

def new_img(name):
    if cap.isOpened():
    _,frame = cap.read()
    cap.release() #releasing camera immediately after capturing picture
    if _ and frame is not None:
        cv2.imwrite('new_img.jpg', frame)
        cv2.destroyAllWindows()
    cap.release()
    path = 'new_img.jpg'
    
img = Image.open(path)
img = img.convert('RGBA')
pix = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 255)
            
text = pytesseract.image_to_string(Image.open('image.png'))
file = open("ocr.txt", "w") 
file.write(text) 
file.close()
print(text)

def texttospeech(filename):
    mytext = 'Welcome to Realtime Image Captionaning cognitive Eyes'
    tfile = open('filename', 'r')
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj = gTTS(text=tfile, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")

textospeech('ocr.txt')

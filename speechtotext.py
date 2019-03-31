import speech_recognition as sr   
r = sr.Recognizer() 
from gtts import gTTS 
import os 
  
with sr.Microphone() as source: 
    r.adjust_for_ambient_noise(source)
    mytext = 'Say Something'
    print( "mytext")
    myobj = gTTS(text=mytext, lang=language, slow=True)
    disclaimer = "error occurs when google could not understand what was said"
    myobj = gTTS(text=disclaimer, lang=language, slow=True)
    audio = r.listen(source) 
          
    try: 
        text = r.recognize_google(audio) 
        print("you said: " + text )

        while True: 

            if 'show' in text:
                os.system("python face_detection.py")
                
            elif 'read' in text:
                os.system('python ocr.py')

            elif "thanks" in text:
                break
            
    except sr.UnknownValueError: 
        disclaimer = "Google Speech Recognition could not understand audio"
        myobj = gTTS(text=disclaimer, lang=language, slow=False)
        print("Google Speech Recognition could not understand audio") 

      
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

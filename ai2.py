#import speech_recognition as sr
import subprocess
import  pyautogui
import time
import webbrowser as web
import wikipedia
import datetime
from playsound import playsound
from datetime import date, timedelta

#r = sr.Recognizer()

#with sr.Microphone() as source:
#    print("Say something: ")
#
#
#    audio = r.listen(source)
#    r.pause_threshold=0.5
def say(text):
 try:

   #text = r.recognize_google(audio)
   print("You said: " + text.lower())
   if text.lower() =="gpt":
       subprocess.call(["say","-v", "Daniel","ok"])
       web.open("https://chatgpt.com")



   elif "youtube" in text.lower() and "search" in text.lower() or "youtube" in text.lower() and "open" in text.lower():
       subprocess.call(["say","-v", "Daniel","ok"])
       web.open_new_tab("https://www.google.com")
       time.sleep(3)
       pyautogui.click(x=750,y=100,duration=0.1)
       pyautogui.typewrite("https://www.youtube.com")
       pyautogui.hotkey("enter")



   elif "delete" in text.lower() and "cube" in text.lower():
       subprocess.call(["say","-v", "Daniel","ok"])
       time.sleep(1)
       subprocess.Popen("open -a blender ",shell=True)
       time.sleep(2)
       pyautogui.click(x=500,y=600,duration=0.1)
       pyautogui.click(x=750,y=600,duration=0.1)
       pyautogui.hotkey("shift","x")
       pyautogui.click(x=750,y=600,duration=0.1)
       pyautogui.click(x=750,y=600,duration=0.1)
       pyautogui.hotkey("shift","a")
       pyautogui.click(x=750,y=600,duration=0.1)
       pyautogui.typewrite("uv")
       pyautogui.hotkey("enter")
       pyautogui.rightClick(x=750,y=600,duration=0.1)
       pyautogui.click(x=750,y=600,duration=0.1)
       subprocess.call(["say","-v", "Daniel","done"])
       playsound("hedwigs-theme.wav")




   elif "vs code online" in text.lower() and "search" in text.lower():
          subprocess.call(["say","-v", "Daniel","ok"])
          web.open_new_tab("https://www.google.com")
          time.sleep(3)
          pyautogui.click(x=750,y=100,duration=0.1)
          pyautogui.typewrite("vscode.dev")
          pyautogui.hotkey("enter")



   elif "amazon" in text.lower() and "open" in text.lower():
             subprocess.call(["say","-v", "Daniel","ok"])
             web.open_new_tab("https://www.google.com")
             time.sleep(3)
             pyautogui.click(x=750,y=100,duration=0.1)
             pyautogui.typewrite("https://www.amazon.in")
             pyautogui.hotkey("enter")



   elif "what is the time" in text.lower() or "time right now" in text.lower() or "what's the time" in text.lower():
               strtime=datetime.datetime.now().strftime("%H:%M")
               print(f"the time is {strtime}")
               subprocess.call(["say","-v", "Daniel",f"the time is {strtime}"])


   else:
            q=text.lower().replace("wikipedia",":-")
            print(q)
            f=open("wiki_data.txt","w")
            f.write("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ")
            f.close()
            ans2=wikipedia.summary(q,sentences=2)
            ans=ans2.replace(";",".")
            ans1=wikipedia.summary(q,sentences=100)
            print(f"According to Sources: {ans1}")
            f=open("wiki_data.txt","w")
            f.write("DATA FROM WIKIPEDIA:-")
            strtime=datetime.datetime.now().strftime("%H:%M")

            f.write(ans1+f"{strtime}")
            f.close()
            subprocess.call(["say","-v", "Samantha",f"{ans}"])
            subprocess.Popen("wiki_data.txt",shell=True)
            playsound("hedwigs-theme.wav")



 



 except ans.Error:
     print("sorry , i can't understand.")
     subprocess.call(["say","-v", "Daniel","sorry , i can't understand."])





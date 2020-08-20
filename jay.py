'''
AS you told us not to use any concept which you not taught,so i havn't use anything otherwise
we can use continue statement to make it simpler.or import datetime module to wish good morning,afternoon & evening according to time.
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
  pyttsx3.speak("Good Morning!")
elif hour>=12 and hour<18:
  pyttsx3.speak("Good Afternoon!")
else:
  pyttsx3.speak("Good Evening!")
'''

import pyttsx3
import os

pyttsx3.speak("I am your virtual assistant. Please tell me how may I help you")
pyttsx3.speak("choose one from the below options")

while True:
  print("What do You want me to do from these options?")
  print("Chrome \nNotepad\nPlayer")
  print("or you wanna quit?")
  print("What can i do for you ? : "  , end='')
  p = input()
  p = p.lower()

  while True:

   if("dont" in p ) or("do not" in p):
     pyttsx3.speak("Ok..then tell me what do you want")
     break
  
   else:
     if (("run" in p) or ("open" in p) or ("execute" in p ))  and (("chrome" in p) or ("browser" in p)):
       pyttsx3.speak("opening chrome............")  
       os.system("chrome")
       break

     elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("notepad" in p) or ("editor" in p)) :
       pyttsx3.speak("opening notepad...........")
       os.system("notepad")
       break
      

     elif (("run" in p) or ("execute" in p ) or ("open" in p)) and (("player" in p) or ("media" in p)):
       pyttsx3.speak("opening window media player...........")
       os.system("wmplayer")
       break
      

     elif  (("exit" in p)  or ("quit" in p) or ("close" in p)):
       pyttsx3.speak("Thanks for using me............Have a good day")
       break

     else:
       pyttsx3.speak("Sorry! I can't fulfill your request. Please try something else.")
       print("Please give a valid input.What to do?")
       break

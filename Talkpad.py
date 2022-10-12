import pyttsx3  
engine = pyttsx3.init() 
print("Enter speech")
while True:
    text=input() 
    engine.say(text) 
    engine.runAndWait() 
    
     
 

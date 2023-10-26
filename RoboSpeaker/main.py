import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")
print("Python text-to-speech test. using win32com.client")

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Pranjal")
    while True:
        x = input("Enter what you want me to pronounce(q for exit): ")
        if x == "q":
            speak.Speak("bye bye friend")
            break
        speak.Speak(x)
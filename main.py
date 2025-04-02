import speech_recognition as sr
import pyttsx3
import os
import subprocess

engine = pyttsx3.init()

engine.setProperty('rate', 150)  
engine.setProperty('volume', 1)  

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the speech recognition service.")
            return None

def create_folder():
    speak("What should I name the folder?")
    folder_name = listen()
    if folder_name:
        try:
            os.makedirs(folder_name)
            speak(f"Folder named {folder_name} has been created.")
        except FileExistsError:
            speak("A folder with that name already exists.")
    else:
        speak("I couldn't hear the folder name.")

def open_camera():
    try:
        subprocess.run("start microsoft.windows.camera:", shell=True)
        speak("Opening Camera.")
    except Exception as e:
        speak("Sorry, I couldn't open the camera.")
        print(e)

def open_chrome():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    if os.path.exists(chrome_path):
        os.startfile(chrome_path)
        speak("Opening Chrome.")
    else:
        speak("Chrome is not installed on this system.")

def main():
    speak("Hello, I am your assistant. How can I help you today?")
    
    while True:
        command = listen()
        if command is None:
            continue
        
        if 'open' in command:
            if 'notepad' in command:
                os.system("notepad")
                speak("Opening Notepad.")
            elif 'calculator' in command:
                os.system("calc")
                speak("Opening Calculator.")
            elif 'camera' in command:
                open_camera()
            elif 'chrome' in command:
                open_chrome()
            else:
                speak("Sorry, I don't know how to open that application.")
        
        elif 'create folder' in command:
            create_folder()

        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        
        else:
            speak("Sorry, I didn't get that command.")

if __name__ == "__main__":
    main()
# executed
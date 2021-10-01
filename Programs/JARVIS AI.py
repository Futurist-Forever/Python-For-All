import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")   

    else:
        speak("Good Evening!")
        print("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you.")
    print("I am Jarvis Sir. Please tell me how may I help you.")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword') # Replace "youremail@gmail.com" to your EMAIL ID & replace "yourpassword" with your password of the email
    server.sendmail('youremail@gmail.com', to, content) # Important: Less secure apps must be enabled in your account to perform this email operation
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube Sir...")
            print("Opening Youtube Sir...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google Sir...")
            print("Opening Google Sir...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stack Over Flow Sir...")
            print("Opening Stack Over Flow Sir...")
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'C:\\Music\\Favorite'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code Sir...")
            print("Opening Visual Studio Code Sir...")
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open word' in query:
            speak("Opening Microsoft Word Sir...")
            print("Opening Microsoft Word Sir...")
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE" # Change the path according to your system
            os.startfile(wordPath)

        elif 'open excel' in query:
            speak("Opening Microsoft Excel Sir...")
            print("Opening Microsoft Excel Sir...")
            excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"  # Change the path according to your system
            os.startfile(excelPath)

        elif 'open powerpoint' in query:
            speak("Opening Microsoft PowerPoint Sir...")
            print("Opening Microsoft PowerPoint Sir...")
            powerpointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"  # Change the path according to your system
            os.startfile(powerpointPath)

        elif 'open chrome' in query:
            speak("Opening Google Chrome Sir...")
            print("Opening Google Chrome Sir...")
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" # Change the path according to your system
            os.startfile(chromePath)

        elif 'open obs studio' or 'open obs' in query:
            speak("Opening OBS Studio Sir...")
            print("Opening OBS Studio Sir...")
            obsPath = "C:\\obs-studio\\bin\\64bit\\obs64.exe" # Change the path according to your system
            os.startfile(obsPath)

        elif 'open arduino' in query:
            speak("Opening Arduino Sir...")
            print("Opening Arduino Sir...")
            arduinoPath = "C:\\Arduino\\arduino.exe"  # Change the path according to your system
            os.startfile(arduinoPath)

        elif 'open oracle' or 'open virtualbox' or 'open virtual box' in query:
            speak("Opening Oracle VM VirtualBox Sir...")
            print("Opening Oracle VM VirtualBox Sir...")
            oraclePath = "C:\\Oracle\\VirtualBox\\VirtualBox.exe" # Change the path according to your system
            os.startfile(oraclePath)

        elif 'open lobe' in query:
            speak("Opening Lobe Sir...")
            print("Opening Lobe Sir...")
            lobePath = "C:\\Lobe\\Lobe.exe" # Change the path according to your system
            os.startfile(lobePath)

        elif 'open discord' in query:
            speak("Opening Discord Sir...")
            print("Opening Discord Sir...")
            discordPath = "C:\\Users\\USER\\AppData\\Local\\Discord\\Update.exe" # Change the path according to your system    

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = "toemail@gmail.com"  # Replace "toemail@gmail.com" to the EMAIL ID that you want to send this email to 
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email.")
                print("Sorry Sir. I am not able to send this email.")    

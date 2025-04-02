import speech_recognition as sr   # It takes data in form of speaks by user and convert it into the text.
import pyttsx3                    # It convert text data into the audioble form and It works as an Engine.
import datetime                   # It is used to know the current date and time.
import webbrowser                 # It is used to open the browser.
import wikipedia                  # It is used to get the knowledge about everything.
import os                         # It is used to handle the file explorer kind of the task
import pyaudio

recognizer = sr.Recognizer()      # It is only Declaration of recorgnizer.Below under it able to listen the user voice after use of the listen(source).
engine = pyttsx3.init()           # It seems like that the engine is started.
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)



def speak(text):                  # Making function so that program can able to speak.
    engine.say(text)              # Program able to speak the data which we given to it in a form of the text.
    engine.runAndWait()           # Program is running and take wait after the execution.


def listen():                     # Making function so that program can able to listen our spoken data.
    with sr.Microphone() as source:  # If sr are able to recognize then must have microphone also which is used as main source.
        print("Listening...")        # print Listening...  .
        recognizer.adjust_for_ambient_noise(source)  # Before listen to user voice , it create an enviornment so that background noise is removed at time of listening.
        audio = recognizer.listen(source)    # Audio variable stores the main message of spoken data of user.
        try:                                 # Use try and except command for trying something command seen below.
            command = recognizer.recognize_google(audio)  # Recognizer recognize our spoken data that stores in an audio variable with refrence of the Google.
            print(f"User said : {command}")   # Printing the command which you telling the Jarvis Assistant.
            return command.title()            # Making the title character of every word present in an our command.If you don't write the title command then program not working .
        except sr.UnknownValueError:          # Making the solution if unknown value error is get.
            speak("Sorry!, I am not understanding that command!")   # If Jarvis doesn’t understand your voice.
            return ""
        except sr.RequestError:               # Making the solution if request error is get.
            speak("Sorry,My speech service is down!")   # If there’s an issue with the speech recognition service.
            return ""
        
def handle_command(command):         # Function to handle the command.
    if "Hello" in command:           # Hello command.                  
        speak("Hello!,How may I assist you ?")
    elif "Tell Me The Current Date" in command :       # Date command.
        currentdate = datetime.datetime.now().strftime("%Y-%m-%d")  
        speak(f"Today date is {currentdate}")
    elif "Tell Me The Current Time" in command:        # Time command.
        currenttime = datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"The Current Time is {currenttime}")
    elif "Search" in command:                           # Search command.
        speak("What do you Want to Search")
        searchquery = listen()
        if searchquery:
            url = f"https://www.google.com/search?q={searchquery}"         # Making the result paste for google.
            webbrowser.open(url)                                           # Using webbrowser to open the url.
            speak(f"So, Here is the result of your query {searchquery}")
    elif 'Open Wikipedia' in command:                                      # Open Wikipedia command.
        speak("What do you want to Search on Wikipedia...")
        command = listen()
        try:
            result = wikipedia.summary(command, sentences=5)
            speak(result)
        except wikipedia.exceptions.PageError:
            speak("No Wikipedia page found for 'plans constant'. Try another search .")
    elif "Open Youtube" in command:      # Youtube command.
        url = "https://www.youtube.com"
        webbrowser.open(url)
        speak("Opening Youtube")
    elif "Open Google" in command:       # Google command.
        url = "https://www.google.com"
        webbrowser.open(url)
        speak("Opening Google")
    elif "Open Gemini" in command:       # Gemini command.
        url = "https://gemini.google.com"
        webbrowser.open(url)
        speak("Opening Gemini")
    elif "Open Deep Seek" in command:    # Deepseek command.
        url = "https://chat.deepseek.com"
        webbrowser.open(url)
        speak("Opening Deepseek")
    elif "Open Instagram" in command:     # Instagram command.
        url = "https://www.instagram.com"
        webbrowser.open(url)
        speak("Opening Instagram")
    elif "Open Medicaps" in command:      # Medicaps command.
        url = "https://www.medicaps.ac.in"
        webbrowser.open(url)
        speak("Opening Medicaps")
    elif "Open Whatsapp" in command:      # Whatsapp command.
        url = "https://www.whatsapp.com"
        webbrowser.open(url)
        speak("Opening Whatsapp")
    elif "Open Chess" in command:         # Chess command.
        url = "https://www.chess.com/home"
        webbrowser.open(url)
        speak("Opening Chess")
    elif "Open Youtube Music" in command: # YoutubeMusic command.
        url = "https://music.youtube.com/"
        webbrowser.open(url)
        speak("Opening YoutubeMusic")     # Spotify command.
    elif "Open Spotify" in command:
        url = "https://open.spotify.com/"
        webbrowser.open(url)
        speak("Opening Spotify")
    elif "Restart" in command:            # Restart command.
        speak("Restarting Your PC")
        os.system("shutdown /r /t 1")
    elif "Shutdown" in command:           # Shutdown command.
        speak("Shutting Down Your PC")
        os.system("shutdown /s /t 1")
    elif "Exit" in command or "Quit" in command:   # Exit or Quit commmand.
        speak("Ok! Good Bye, Have a Good Day!")
        exit()
    else:                                          # Else command.
        speak("Sorry ! I do not understand what you are saying !")


# Main function.
if __name__ == "__main__":               # Important part in jarvis assistant program.
    speak("Hello!, I am Jarvis , How may I assist you Today!")
    while True:                          # Using while loop for infinitely running the program.
        command = listen()
        if command:                      # If statement.
            handle_command(command)
    






        






        
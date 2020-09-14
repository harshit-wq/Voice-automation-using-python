import pyttsx3
import datetime
import speech_recognition  as sr
import wikipedia
import webbrowser
from Time import printWords

engine=pyttsx3.init('espeak')

def speak(audio):
    engine.say(audio)
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 145)
    engine.setProperty('volume', 0.5)
    engine.setProperty('voice', voices[2].id)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Eveneing!')
        
    speak("Jarvis at your command! sir!")    

def takeCommand():
    '''
    it takes microphone input and returns string
    '''

    recon=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        recon.pause_threshold=1   
        audio=recon.listen(source)

    try:
        print('Recorganizing')
        query=recon.recognize_google(audio, language='en-in')
        print('User said:', query)
    except Exception as e:
        print(e)
        print("Please say that again and check your internet connection")    
        return None

    return query

def get_wikipedia(query):
    speak('Searching wikipedia')
    query=query.replace('wikipedia', '')
    results=wikipedia.summary(query, sentences=2)
    print(results)
    speak('According to wikipedia')
    speak(results)
    return

def open_youtube():
    c=webbrowser.get('firefox')
    c.open_new_tab('www.youtube.com')

def open_google():
    c=webbrowser.get('firefox')
    c.open_new_tab('www.google.com')

def open_facebook():
    c=webbrowser.get('firefox')
    c.open_new_tab('www.facebook.com')

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand()
        try:
            if 'wikipedia' in query.lower():
                get_wikipedia(query)
            elif 'open youtube' in query.lower():
                open_youtube()
            elif 'open google' in query.lower():
                open_google()
            elif 'open facebook' in query.lower():
                open_facebook()
            elif 'say' in query.lower():
                x=query.lower().find('say')
                speak(query[x+3:])
            elif 'time now' in query.lower():
                x="Its"+" "+' '.join(list(printWords(datetime.datetime.now().hour, datetime.datetime.now().minute)))
                print(x)
                speak(x)
        except:
            pass

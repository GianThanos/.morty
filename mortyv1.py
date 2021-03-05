import tkinter as tk
import wolframalpha as wolf
import pyttsx3 as pt
import speech_recognition as sr
import webbrowser
import random
import sys
import wikipedia
import datetime

# ----------------------------------------------------------------------------------------------------------imputs---------
client = wolf.Client('TU3RTW-WYW534WPPR')
engine = pt.init()
speakb = 1
voiceb = 1
# ----------------------------------------------------------------------------------------------------------DEF--------

def recognition():
    while True:
        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            text.insert(tk.END, 'okey\n')
            if speakb == 2:
              speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            text.insert(tk.END, 'okey\n')
            if speakb == 2:
              speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            text.insert(tk.END, 'okey\n')
            if speakb == 2:
              speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            rc= random.choice(stMsgs)
            text.insert(tk.END, rc +'\n')
            if speakb == 2:
              speak(rc)

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            text.insert(tk.END, 'okey\n')
            text.insert(tk.END, 'Bye gaz, have a good day.\n')
            if speakb == 2:
              speak('okay')
              speak('Bye gaz, have a good day.')
            sys.exit()

        elif 'hello' in query:
            text.insert(tk.END, 'Hello gaz\n')
            if speakb == 2:
              speak('Hello gaz')

        elif 'bye' in query:
            text.insert(tk.END, 'Bye gaz, have a good day.\n')
            if speakb == 2:
              speak('Bye gaz, have a good day.')
            sys.exit()
        else:
            query = query
            text.insert(tk.END, 'Searching...\n')
            if speakb == 2:
              speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    text.insert(tk.END, 'Got it.\n')
                    text.insert(tk.END, results + '\n')
                    if speakb == 2:
                      speak('Got it.')
                      speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    text.insert(tk.END, 'Got it.\n')
                    text.insert(tk.END, 'WIKIPEDIA says - \n')
                    text.insert(tk.END, results + '\n')
                    if speakb == 2:
                      speak('Got it.')
                      speak('WIKIPEDIA says - ')
                      speak(results)

            except:
                webbrowser.open('www.google.com')
        text.insert(tk.END, 'Next Command! Sir!\n')
        if speakb == 2:
          speak('Next Command! Gaz!')

def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        text.insert(tk.END, 'Listening...\n')
        if speakb == 2:
            speak('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        userprint = ('User: ' + query + '\n')
        text.insert(tk.END, userprint)
        if speakb == 2:
            speak(userprint)


    except sr.UnknownValueError:

        text.insert(tk.END, 'Sorry bro! I didn\'t get that!\n')
        text.insert(tk.END, 'Listening...\n')
        if speakb == 2:
            speak('Sorry bro! I didn\'t get that!')
            speak('Listening...')
        myCommand()
    return query



#def voicerecoff():
    #global voiceb
    #text.insert(tk.END, 'Voice Rec is now OFF\n')
    #text.insert(tk.END, 'How i can help you?\n')
    #if speakb == 2 :
        #speak('Voice Rec is now OFF')
        #speak('How i can help you?')
   # voiceb = 1


def voicerecon():
    global voiceb

    voiceb = 2
    text.insert(tk.END, 'Voice Rec is now ON\n')
    if speakb == 2:
      speak('Voice Rec is now ON')
      speak('How i can help you?')
    text.insert(tk.END, 'How i can help you?\n')
    recognition()


def backtolifeoff():
    global speakb
    text.insert(tk.END, 'Back to life is now OFF\n')
    text.insert(tk.END, 'How i can help you?\n')
    speak('Back to life is now OFF')
    speakb = 1


def speak(text):
    engine.say(text)
    engine.runAndWait()


def backtolifeon():
    global speakb

    speakb= 2
    text.insert(tk.END, 'Back to life is now ON\n')
    speak('Back to life is now ON')

    text.insert(tk.END, 'How i can help you?\n')
    speak('How i can help you?')



def brain():
    global output

    query = textinput.get()
    textinput.delete(0, tk.END)
    if query == 'stop':
        text.insert(tk.END, 'Bye gaz, have a good day.\n')
        if speakb == 2:
            speak('Bye gaz, have a good day.')
        sys.exit()

    res = client.query(query)
    output = next(res.results).text


    que = ('>>>Question: ' + query + '\n' )
    text.insert(tk.END, que)
    if speakb==2:
        speak(query)

    ans = str('>>>Answer:  ' + output + '\n' )
    text.insert(tk.END, ans)
    if speakb==2:
        speak(output)

    text.insert(tk.END, '\nHow i can help you?\n\n')
    if speakb == 2:
        speak('How i can help you?')

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        text.insert(tk.END, 'Good Morning!\n')

    if currentH >= 12 and currentH < 18:
        text.insert(tk.END, 'Good afternoon!\n')

    if currentH >= 18 and currentH != 0:
        text.insert(tk.END, 'Good evening!\n')

# ------------------------------------------------------------------------------------------------parathiro main------

def main():
    global text
    global textinput

    main= tk.Tk()
    main.geometry('900x600')
    main.title('.morty')

    text= tk.Text(main)
    text.place(relx=0, rely=0, relwidth=0.8, relheight=0.95)

    textinput= tk.Entry(main)
    textinput.place(relx=0, rely=0.95, relwidth=0.7, relheight=0.05)

    buttonsend= tk.Button(main,text='Send',command=brain)
    buttonsend.place(relx=0.7, rely=0.95, relwidth=0.1, relheight=0.05)

    greetMe()
    text.insert(tk.END, 'Welcome, gaz!\n')
    text.insert(tk.END, 'How i can help you?\n\n')







# GIA THN LISTA STA DEKSIA

    frame= tk.Frame(main,bg='lightblue')
    frame.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

    labelframe= tk.Label(frame,bg='lightblue',text=('Functions'), font=("Courier", 20))
    labelframe.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    buttonbtl= tk.Button(frame,bg ='lightgray',text='Back to life ON',command=backtolifeon)
    buttonbtl.place(relx=0, rely=0.1, relwidth=1, relheight=0.05)

    buttonbt2 = tk.Button(frame, bg='lightgray', text='Back to life OFF',command=backtolifeoff)
    buttonbt2.place(relx=0, rely=0.15, relwidth=1, relheight=0.05)

    buttonbt3= tk.Button(frame,bg ='lightgray',text='Voice Rec ON',command=voicerecon)
    buttonbt3.place(relx=0, rely=0.25, relwidth=1, relheight=0.05)

    #buttonbt4 = tk.Button(frame, bg='lightgray', text='Voice Rec OFF')
    #buttonbt4.place(relx=0, rely=0.3, relwidth=1, relheight=0.05)

    main.mainloop()

# ----------------------------------------------------------------------o elenxos username kai run login window---------

def connect():
    global chuser
    global chpass
    chuser = entryuser.get()
    chpass = entrypass.get()

    if (chuser == 'gaz'):
        if (chpass == '123123'):
            root.destroy()
            main()


def login():
  global entrypass
  global entryuser
  global root
  root=tk.Tk()
  root.title('login')
  root.geometry('600x450')




  image= tk.PhotoImage(file="ravenlogin.png")
  label = tk.Label(root, image=image)
  label.place(relx=0, rely=0, relwidth=1, relheight=1)

  label1= tk.Label(root, text='.morty',bg='lightgray')
  label1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

  labeluser=tk.Label(root,text='Username',bg='lightgray')
  labeluser.place(relx=0, rely=0.7, relwidth=0.15, relheight=0.05)

  entryuser= tk.Entry(root)
  entryuser.place(relx=0.15, rely=0.7, relwidth=0.15, relheight=0.05)

  labeluser=tk.Label(root,text='Password',bg='lightgray')
  labeluser.place(relx=0, rely=0.75, relwidth=0.15, relheight=0.05)

  entrypass= tk.Entry(root)
  entrypass.config(show="*")
  entrypass.place(relx=0.15, rely=0.75, relwidth=0.15, relheight=0.05)

  buttonconnect= tk.Button(root,text= ('Connect'), bg='lightgray',command=connect)
  buttonconnect.place(relx=0.1, rely=0.8, relwidth=0.15, relheight=0.05)

  root.mainloop()

login()
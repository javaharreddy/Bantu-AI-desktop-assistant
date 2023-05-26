#these are the modules used in the whole bantu ai
import datetime

import speech_recognition as sr
import win32com.client
import webbrowser
import os
from googletrans import Translator
import openai
import random

#it is the speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def playsong():
        try:
            files=[r'C:\Users\91934\Desktop\music\[iSongs.info] 01 - Yedhi Yedhi.mp3',r'C:\Users\91934\Desktop\music\[iSongs.info] 04 - Laayi Laayi.mp3']
            file_path=files[random.randint(0,len(files)-1)]
            os.startfile(file_path)
        except OSError as e:
            print(f"Error opening the file: {e}")
def play_youtube_song(song_name):
    query = song_name # Modify the query to enhance search accuracy
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
def translate_text(text,source,destination):
    translator = Translator()
    translation = translator.translate(text, src=source, dest=destination)
    translated_text = translation.text
    return translated_text
def ai(prompt):
    openai.api_key = "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"
    text = f"{prompt} \n **************************************************************************** \n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text+=response["choices"][0]['text']
    if not os.path.exists("openai"):
        os.mkdir("openai")
    speaker.speak("generating the file in openai folder for "+prompt)
    with open(f"openai/prompt- {prompt[:30]}","w") as f:
        f.write(text)

chatstr=''
def chat(prompt,name,enortel):
    global chatstr
    openai.api_key = "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"
    chatstr+=f"{name} : {prompt}\nbantu : "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print('bantu : ',end='')
    if(enortel==0):
        print(translate_text(response["choices"][0]['text'],'en','te'))
    else:
        print(response["choices"][0]["text"][1:])
    speaker.speak(response["choices"][0]['text'])
    chatstr += response["choices"][0]['text']
def takeCommand(enortel):
    r = sr.Recognizer()
    with sr.Microphone(2) as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            if enortel==0:
              query = r.recognize_google(audio, language="te-in")
            else:
              query = r.recognize_google(audio, language="en-in")
            return query
        except:
            return "sorry buntoo can't understand"
if __name__ == '__main__':
    print('bantu : Hi I am bantu AI')
    speaker.speak("Hi I am buntoo AI")
    speaker.speak("What is your name?")
    name=str(input("bantu : enter your name\nyou : "))
    speaker.speak("Hi "+name)
    speaker.speak("enter 0 for telugu and enter 1 for english")
    enortel=int(input())
    if enortel==0:speaker.speak("ok you ask commands in telugu i can understand telugu but i will speak in english")
    else:speaker.speak("ok let us talk in english")
    while True:
        print('bantu : listening....')
        if enortel==0:
            quer = takeCommand(enortel)
            print(name+" : "+quer)
            query = translate_text(quer,'te','en')
        else:
            query = takeCommand(1)
            print(name+" : "+query)
        query=query.lower()
        sites=[["github","https://github.com/"],["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"],["chat","https://chat.openai.com/"],["mail","https://mail.google.com/"]]
        for site in sites:
            if f"open {site[0]}" in query:
                webbrowser.open(site[1])
                speaker.speak("opening "+site[0])
                print("bantu : opening "+site[0])
        else:
         if "play song"==query or query=="play a song":
            speaker.speak('ok '+name+' playing a random song from your playlist')
            print("bantu : ok"+name+' playing a random song from your playlist')
            playsong()
         elif ("song" in query )or ("play" in query):
            speaker.speak("ok "+name+" playing "+" that song in youtube")
            print("bantu : ok "+name+" playing "+" that song in youtube")
            play_youtube_song(query)
         elif "time" in query:
            time=datetime.datetime.now().strftime("%I:%M %p")
            speaker.speak("ok "+name+" the time is "+time)
            print("bantu : the time is "+time)
         elif "using artificial intelligence" in query:
            ai(query)
         else:
            chat(query,name,enortel)
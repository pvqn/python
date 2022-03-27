import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("say something")
    audio = r.listen(source)
    text = r.recognize_google(audio)

    if "hello" in text:
        print("user: {}".format(text))
        engine.say("hello nhu")
        engine.runAndWait()
        print("siri: hello nhu")
    if "something" in text:
        print("user: {}".format(text))
        engine.say("hello world")
        engine.runAndWait()
        print("siri: hello world")
    if "bye" in text:
        engine.say("goodbye")
        engine.runAndWait()

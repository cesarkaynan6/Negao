# Our main file.

import speech_recognition as sr

# cria um reconhecedor
r = sr.Recognizer()

# Abrir o microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Define como fonte de audio

        print(r.recognize_google(audio, language='pt'))

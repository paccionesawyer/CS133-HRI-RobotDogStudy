#https://hackernoon.com/how-to-convert-speech-to-text-in-python-q0263tzp

import speech_recognition as sr

recognizer = sr.Recognizer()

''' recording the sound '''
with sr.Microphone() as source:
    
    while True:
        try:
            recorded_audio = recognizer.listen(source, timeout=4, phrase_time_limit=2)
        except sr.WaitTimeoutError:
            continue

        try:
            #print("Recognizing the text")
            #if recorded_audio is not None:
            text = recognizer.recognize_google(
                    recorded_audio, 
                    language="en-US"
                )
            decodedText = "Decoded Text : {}".format(text)
            decodedText = decodedText.lower()
            words = decodedText.split(" ")
            if "sit" in words:
                print("sit")
                breaks
            elif "stand" in words:
                print("stand")
                break
            elif "come" in words:
                print("come")
                break
            elif "spin" in words:
                print("spin")
                break
            else:
                continue
        except Exception as ex:
            print(ex)
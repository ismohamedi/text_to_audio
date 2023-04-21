from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

def convert_text_to_audio(text: str, name:str):
    audio =  name + ".wav"

    # by default we use english
    language = "sw"

    convert = gTTS(text=text,lang=language,slow=False)
    convert.save(audio)
    playsound(audio)
    
    
def convert_audio_to_text():
    recognizer = sr.Recognizer()
    language = "sw"
    with sr.AudioFile('ismailiSw.wav') as source:
    
       audio_text = recognizer.listen(source)
       try:
            # using google speech recognition
            text = recognizer.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)
       except:
            print('Sorry.. run again...')
    
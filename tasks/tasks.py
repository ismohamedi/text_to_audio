from gtts import gTTS
from playsound import playsound

def convert_text_to_audio(text: str, name:str):
    audio =  name + ".mp3"

    # by default we use english
    language = "en"

    convert = gTTS(text=text,lang=language,slow=False)
    convert.save(audio)
    playsound(audio)
    
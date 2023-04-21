from fastapi import FastAPI
from tasks.tasks import convert_audio_to_text, convert_text_to_audio

app = FastAPI(title="Text to Audio App", docs_url="/docs", redoc_url=None)

@app.post('/convert/{text}/{audio_name}',tags=["Convertion"])
def convert(text:str,audio_name:str):
    return convert_text_to_audio(text,audio_name)

@app.post('/convert-audio-to-text',tags=["Convertion"])
def convert_audio_to_text_():
    return convert_audio_to_text()
from fastapi import FastAPI, HTTPException, Response
from transformers import pipeline
from google.cloud import texttospeech

app = FastAPI()

# Load translation model (adjust model name as needed)
try:
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es") # Example: English to Spanish
except Exception as e:
    print(f"Error loading translation model: {e}")
    translator = None

# Initialize Google Cloud Text-to-Speech client
try:
    tts_client = texttospeech.TextToSpeechClient()
except Exception as e:
    print(f"Error initializing TTS client: {e}")
    tts_client = None

@app.post("/tts")
async def text_to_speech(text: str, target_language: str = "es", source_language: str = "en"):
    if translator is None or tts_client is None:
        raise HTTPException(status_code=500, detail="Translation or TTS service not available.")

    try:
        # Translate text
        translated_text = translator(text)[0]["translation_text"]

        # Synthesize speech using Google Cloud TTS
        synthesis_input = texttospeech.SynthesisInput(text=translated_text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=target_language, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        response = tts_client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        return Response(content=response.audio_content, media_type="audio/mpeg")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "_main_":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
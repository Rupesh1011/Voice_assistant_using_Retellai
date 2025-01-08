import requests
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import io

# Retellai Webhook URL (from Make.com)
retellai_webhook_url = "YOUR_MAKE_COM_WEBHOOK_URL"
retellai_voice_url = "YOUR_RETELL_AI_VOICE_API_URL"  # Replace with Retell.ai Voice API URL

# Record audio from microphone
def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio_data = recognizer.listen(source)
        print("Recording complete.")
        audio_wav = audio_data.get_wav_data()  # Record audio as WAV format
        return audio_wav

# Send audio to Make.com Webhook
def send_audio_to_make_webhook(audio_data):
    files = {'file': ('audio.wav', audio_data, 'audio/wav')}
    response = requests.post(retellai_webhook_url, files=files)
    return response.json()  # Get the response from Make.com scenario

# Send response text to Retell.ai Voice API for speech output
def send_text_to_retellai_voice(response_text):
    payload = {
        "text": response_text,  # The text that is need to be converted to speech
        "voice": "en_us_male", 
        "language": "en" 
    }
    response = requests.post(retellai_voice_url, json=payload)
    if response.status_code == 200:
        audio_url = response.json().get("audio_url")
        if audio_url:
            audio_data = requests.get(audio_url).content  # Download the audio file
            return audio_data  # Return audio data to play
        else:
            print("No audio URL returned.")
    else:
        print("Failed to generate speech.")
        return None

# Play the generated audio using pydub
def play_audio(audio_data):
    audio = AudioSegment.from_wav(io.BytesIO(audio_data))  
    play(audio) 

# Process the response from Make.com
def process_response(response_data):
    if 'response_text' in response_data:
        print("Assistant says:", response_data['response_text'])
        audio_data = send_text_to_retellai_voice(response_data['response_text'])  # Convert text to speech
        if audio_data:
            play_audio(audio_data)  # Play the generated audio
    else:
        print("No response text from assistant.")
        audio_data = send_text_to_retellai_voice("Sorry, I couldn't understand that.")  # Fallback message
        if audio_data:
            play_audio(audio_data)  # Play the fallback audio

# Main Voice Assistant Logic
def voice_assistant():
    while True:
        audio_data = record_audio()  # Step 1: Record audio
        response_data = send_audio_to_make_webhook(audio_data)  # Step 2: Send audio to Make.com via Webhook
        process_response(response_data)  # Step 3: Process and play the response audio

# Run the assistant
voice_assistant()

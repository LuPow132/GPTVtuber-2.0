import AUTH_KEY
import azure.cognitiveservices.speech as speechsdk

pitch = "+20Hz"
tts_model = "en-US-JaneNeural"
AzureApiKey = AUTH_KEY.AZURE_KEY

speech_config = speechsdk.SpeechConfig(subscription=AzureApiKey, region="southeastasia")
audio_config = speechsdk.audio.AudioOutputConfig(filename="opening.wav")
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=audio_config)

text = "science bitch! I'm go now fuck you all! Bye"

ssml_string = f'<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xml:lang="en-US"><voice name="{tts_model}" style="Shouting"><prosody pitch="{pitch}">{text}</prosody></voice></speak>'
result = speech_synthesizer.speak_ssml_async(ssml_string).get()
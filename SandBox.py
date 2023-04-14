import AUTH_KEY
import azure.cognitiveservices.speech as speechsdk
import text2emotion as te

AzureApiKey = AUTH_KEY.AZURE_KEY

speech_config = speechsdk.SpeechConfig(subscription=AzureApiKey, region="southeastasia")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=audio_config)

def speakEN(text,emotions):
    ssml_string = f'<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xml:lang="en-US"><voice name="en-US-JaneNeural" style="{emotions}"><prosody pitch="+20Hz">{text}</prosody></voice></speak>'
    result = speech_synthesizer.speak_ssml_async(ssml_string).get()
while True:
    text = input("Text input: ")
    emotion_dict = te.get_emotion(text)

    # Find the highest score and its corresponding emotion
    max_emotion = max(emotion_dict, key=emotion_dict.get)

    # Print the highest score and its corresponding emotion
    print(f"Highest score: {emotion_dict[max_emotion]:.2f} for {max_emotion}")

    if "whisper" in text or "whispering" in text:
        emotion = "Whispering"
    elif "shouting" in text or "shout" in text or "yell" in text:
        emotion = "Shouting"
    elif max_emotion == "Happy":
        emotion = "Cheerful"
    elif max_emotion == "Angry":
        emotion = "Angry"
    elif max_emotion == "Surpise":
        emotion = "Excited"
    elif max_emotion == "Sad":
        emotion = "Sad"
    elif max_emotion == "Fear":
        emotion = "Terrified"
    else:
        emotion = "Default"

    print(emotion)
    speakEN(text,emotion)
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

# Initialize the recognizer and translator
r = sr.Recognizer()
translator = Translator()

def recognize_translate_play():
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)

        try:
            speech_text = r.recognize_google(audio)
            print("You said:", speech_text)

            # Translate the speech to English
            translated_text_en = translator.translate(speech_text, dest='en').text
            print("Translated text (English):", translated_text_en)

            # Translate the speech to Japanese
            translated_text_ja = translator.translate(speech_text, dest='ja').text
            print("Translated text (Japanese):", translated_text_ja)

            # Convert translated text to speech in Japanese
            voice = gTTS(text=translated_text_ja, lang='ja')
            voice.save("voice.mp3")
            playsound("voice.mp3")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")

# Call the function to run the translation
recognize_translate_play()

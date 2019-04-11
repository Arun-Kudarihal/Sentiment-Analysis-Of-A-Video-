import speech_recognition as sr
import wave
r = sr.Recognizer()

import subprocess
#Change the file names below 
video_file_name = "Sadhguru.mp4"
output_audio_file_name = "audio.wav"
command = "ffmpeg -i " + video_file_name + " -ab 160k -ac 2 -ar 44100 -vn " + output_audio_file_name
subprocess.call(command, shell=True)

from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio.wav")

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio)
    print("The audio said ==> " + text)
except:
    print("Google Speech Recognition could not understand audio") 
''', analyzer=NaiveBayesAnalyzer()'''

from textblob import TextBlob
#from textblob.sentiments import NaiveBayesAnalyzer
opinion = TextBlob(text)
print(opinion.sentiment)

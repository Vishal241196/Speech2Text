#import packages
import librosa
import librosa.display
import soundfile as sf
import speech_recognition as sr
from pydub import AudioSegment
import numpy as np
import io

def preprocess_audio(input_file, output_file):
    # Load audio file
    audio, sr_orig = librosa.load(input_file, sr=None)

    # Voice Activity Detection (VAD)
    non_silent_intervals = librosa.effects.split(audio)

    # Noise Removal
    audio_denoised = np.concatenate([audio[start:end] for start, end in non_silent_intervals])

    # Preemphasis
    audio_preemphasized = librosa.effects.preemphasis(audio_denoised)

    # Normalization
    audio_normalized = librosa.util.normalize(audio_preemphasized)

    # Save preprocessed audio
    sf.write(output_file, audio_normalized, sr_orig)

def speech2Text(file):
    # Define the paths for preprocessed audio
    preprocessed_file = "denoised_normalized_audio.wav"

    # Preprocess audio
    preprocess_audio(file, preprocessed_file)

    # Recognize speech from the preprocessed audio
    r = sr.Recognizer()

    with sr.AudioFile(preprocessed_file) as source:
        audio = r.record(source)

    try:
        textdata = r.recognize_google(audio)
        print("Text data: " + textdata)
        return textdata

    except sr.UnknownValueError:
        print("Audio Error")

    except sr.RequestError as e:
        print("Could not request results from Google API; {0}".format(e))



#Write results to a txt file
#file = open("result.txt","w")
#file.write(textdata)
#file.writelines(L) 
#file.close()

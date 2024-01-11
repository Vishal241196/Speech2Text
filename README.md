# Speech-to-Text Web Application

## Overview

This is a simple web application built using Flask for Speech-to-Text conversion. Users can upload a WAV audio file, and the application uses Google's Speech Recognition API to convert the audio to text.

## Project Structure

- `clientApp.py`: Flask web application.
- `speechToText.py`: Contains functions for preprocessing audio and converting speech to text.
- Inside templets folder->`index.html`: HTML template for the user interface.
- Inside Speech2Text_utils folder-> `utils.py`: Utility functions.

## Dependencies

- Flask
- librosa
- soundfile
- speech_recognition
- pydub

## Setup and Usage

1. Install dependencies using `pip install -r requirements.txt`.
2. Run the Flask application using `python clientApp.py`.
3. Access the application in your web browser at `http://localhost:5000`.

## Example

1. Open the web application.
2. Upload a WAV file.
3. Click the "Predict" button.
4. View the converted text in the result box.

## Credits

- Flask: [Link to Flask](https://flask.palletsprojects.com/)
- librosa: [Link to librosa](https://librosa.org/doc/main/index.html)
- Google Speech Recognition API: [Link to Google Speech Recognition](https://pypi.org/project/SpeechRecognition/)

## Challenges

During the development of this Speech-to-Text web application, we encountered several challenges related to the quality and clarity of the audio data. These challenges included:

1. **Background Noise:**
   - Audio files often contain background noise that can interfere with speech recognition accuracy.

2. **Variable Volume Levels:**
   - Inconsistent volume levels across different audio files can impact the performance of the speech recognition system.

## Solutions

To overcome these challenges, we implemented the following preprocessing techniques:

#### 1. Voice Activity Detection (VAD)

Voice Activity Detection is a crucial step in filtering out non-speech segments from the audio. This helps in focusing on relevant parts of the audio for speech recognition.

#### 2. Noise Removal

After identifying non-speech segments through VAD, we applied noise removal techniques to reduce the impact of background noise. This ensures that the speech recognition model primarily focuses on the user's voice.

#### 3. Preemphasis

Preemphasis is applied to the audio signal to amplify high frequencies, enhancing the clarity of the speech signal. This step improves the overall quality of the audio data before feeding it into the speech recognition system.

#### 4. Normalization

Normalization is performed to standardize the volume levels across different audio files. This step ensures consistent input to the speech recognition model, irrespective of the original volume variations.

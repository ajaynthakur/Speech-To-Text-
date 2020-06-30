# Speech-To-Text(English & Marathi)
Speech to Text is simple project to convert Speech through Microphone to text by Using PyAudio Library.Here I am using Google Speech recognition API for conversion.

A) Pre_requsites : 
1) Python :
Python 2.6, 2.7, or 3.3+ (required)

2) PyAudio: PyAudio Library is essential.PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone).
You can install through following command:
pip install PyAudio
OR Visit
 https://pypi.org/project/PyAudio/
 
3) Speech Recognition:
You can install through following command:
pip install SpeechRecognition
OR Visit
https://pypi.org/project/SpeechRecognition/ 
                 
B) Steps for Speech to Text:
1) Import Speech Recognition Library
2) To recognize the speech initialize the recognizer class
3) By using the microphone class recognize the audio.
4)Convert Audio to text by using recognize_google API.

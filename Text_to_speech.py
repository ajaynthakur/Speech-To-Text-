#import the speech_recognition library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
#we are using Microphone as Source
# listening the speech and store in input_audio variable
#Microphone Class is used
with sr.Microphone() as source:
    print("Speak")
    input_audio = r.listen(source)

    #sleep(3);
    #print("Speak")

    print("Lets Speak")
#We are using recognize_google method for ebabling the API function. If APi is disable it will throw error.

    try:
        # By using google speech recognition
        print("Text: "+r.recognize_google(input_audio))
        print("Text: "+r.recognize_google(input_audio, language = "mr-IN"))
    except:
         print("Sorry, I didn't hear you")

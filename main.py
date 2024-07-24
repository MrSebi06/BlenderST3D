import speech_recognition as sr

# Initialize the recognizer 
r = sr.Recognizer()

# Loop infinitely for user to speak
while True:
    # Exception handling to handle exceptions at the runtime
    try:
        # Use the microphone as source for input.
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)

            MyText = r.recognize_sphinx(source2)

            MyText = MyText.lower()

            print("Did you say:", MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occurred")

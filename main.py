import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Loop infinitely for user to speak
while True:
    # Exception handling to handle exceptions at runtime
    try:
        # Use the microphone as source for input.
        with sr.Microphone() as source2:
            # Wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            print("Listening...")

            # Listens for the user's input
            audio2 = r.listen(source2)

            # Using Sphinx to recognize audio
            MyText = r.recognize_sphinx(audio2)
            MyText = MyText.lower()

            print("Did you say:", MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occurred")

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

    except Exception as e:
        print(f"An error occurred: {e}")

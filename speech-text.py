import speech_recognition as sr

def recognize_speech_from_mic():
	# Initialize recognizer class (for recognizing the speech)
	recognizer = sr.Recognizer()

	# Use the microphone as source for input.
	with sr.Microphone() as source:
		print("Listening...")
		# Adjust the recognizer sensitivity to ambient noise and record audio
		recognizer.adjust_for_ambient_noise(source, duration=0.5)
		audio = recognizer.listen(source)

	# Recognize speech using Google Web Speech API
	try:
		print("Recognizing...")
		text = recognizer.recognize_google(audio)
		print("You said: " + text)
	except sr.UnknownValueError:
		print("Google Web Speech API could not understand audio")
	except sr.RequestError as e:
		print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
	recognize_speech_from_mic()
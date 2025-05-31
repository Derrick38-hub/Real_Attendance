import pyttsx3

engine = pyttsx3.init()

# List available voices
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name}")

# Use a female or default voice
engine.setProperty('voice', voices[0].id)  # You can change index

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

engine.say("Welcome back, Derrick")
engine.runAndWait()
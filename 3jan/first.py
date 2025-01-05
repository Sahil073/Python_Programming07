import speech_recognition as sr

# List all available microphones and their indices
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with index {index}: {name}")

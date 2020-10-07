import speech_recognition as sr
import os

r = sr.Recognizer()

text_array = []

files_count = len(os.listdir("./data"))

for i in range(files_count):
    name = "data/" + str(i) + ".wav"
    print(name)
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    try: 
        text = r.recognize_google(audio, language='ja-JP')
        print(text)
        text_array.append(text)
    except:
        pass

print(text_array)

output_array = []

for text in text_array:
    output_array = output_array + text.split(" ")

print(output_array)

with open("sample.txt", mode="w") as f:
    f.write("\n".join(output_array))

import speech_recognition as sr
 
r = sr.Recognizer()

text_array = []

for i in range(11):
    name = "sample" + str(i) + ".wav"
    print(name)
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    try: 
        text = r.recognize_google(audio, language='ja-JP')
        print(text)
        text_array.append(text)
    except:
        pass

# with sr.AudioFile("sample.wav") as source:
#     audio = r.record(source)
#  
# text = r.recognize_google(audio, language='ja-JP')
 
print(text_array)

import pyttsx3
import speech_recognition as sr

# 要转换的音频源文件
AUDIO_FILE = "chinese.aiff"

# 语种
languageType = "zh-CN"

# 定义SpeechRecognition对象
r = sr.Recognizer()


# 获取音频源文件中的数据
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

'''

# 从麦克风获取音频
with sr.Microphone() as source:
    # 校准环境噪声水平的energy threshold
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

# 把音频写入.wav文件
with open("speech.wav", "wb") as f:
    f.write(audio.get_wav_data())
'''

'''
# 把音频写入.raw文件
with open("speech.raw", "wb") as f:
    f.write(audio.get_raw_data())

# 把音频写入.aiff文件
with open("speech.aiff", "wb") as f:
    f.write(audio.get_aiff_data())

# 把音频写入.flac文件
with open("speech.flac", "wb") as f:
    f.write(audio.get_flac_data())
'''

def speech_to_text():
    # CMU Sphinx
    try:
        print(r.recognize_sphinx(audio, language = languageType))
        return r.recognize_sphinx(audio, language = languageType)
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


def text_to_speech(Sentence):
    engine = pyttsx3.init()
    engine.say(Sentence)
    engine.runAndWait()

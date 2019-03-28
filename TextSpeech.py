import speech_recognition as sr

from aip import AipSpeech

import requests
import time
import hashlib
import base64
import os
import json

import pyttsx3

# 要转换的音频源文件
AUDIO_FILE = "chinese.wav"

# 定义SpeechRecognition对象
r = sr.Recognizer()

# 从麦克风获取音频并写入文件
def record():
    with sr.Microphone() as source:
        # 校准环境噪声水平的energy threshold
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # 把音频写入.wav文件
    with open("speech.wav", "wb") as f:
        f.write(audio.get_wav_data())
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
    return audio

def speech_to_text_cmu():
    # 语种
    languageType = "zh-CN"

    # 获取音频源文件中的数据
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    # 或从麦克风读入
    # audio = record()

    try:
        print(r.recognize_sphinx(audio, language = languageType))
        return r.recognize_sphinx(audio, language = languageType)
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


def speech_to_text_baidu():
    # record()
    # time.sleep(5)
    # https://cloud.baidu.com/product/speech 申请api
    APP_ID = "15879864"
    API_KEY = "3kvoYsDh8fGWSqdInnbcOlif"
    SECRET_KEY = "qjqhdNAdFHcGNmpsi0fiTgWwQsak1HuW"

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(AUDIO_FILE):
        with open(AUDIO_FILE, 'rb') as fp:
            return fp.read()

    result = client.asr(get_file_content(AUDIO_FILE), 'pcm', 16000, {
        'dev_pid': 1537, # 识别普通话，使用输入法模型
    })

    print(result['result'][0])
    return result['result'][0]


def speech_to_text_ifly():
    URL = "http://api.xfyun.cn/v1/service/v1/iat"
    APPID = "5c9c862c"
    API_KEY = "161f98a73874d899cab3d8a4f646a722"

    # aue：音频格式
    # engineType：引擎类型 （sms16k（16k采样率普通话音频）、sms8k（8k采样率普通话音频））
    def getHeader(aue, engineType):
        # curTime：当前UTC时间戳
        curTime = str(int(time.time()))
        
        param = "{\"aue\":\"" + aue + "\"" + ",\"engine_type\":\"" + engineType + "\"}"
        paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8') # Base64编码

        # checkSum：令牌 出于安全性考虑，每个checkSum的有效期为5分钟(用curTime计算)
        m2 = hashlib.md5()
        m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
        checkSum = m2.hexdigest()

        # 请求头
        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': APPID,
            'X-CheckSum': checkSum,
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        return header

    def getBody(filepath):
        binfile = open(filepath, 'rb') # 二进制
        data = {'audio': base64.b64encode(binfile.read())} # Base64编码
        return data

    aue = "raw"
    engineType = "sms16k"

    r = requests.post(URL, headers=getHeader(aue, engineType), data=getBody(AUDIO_FILE))
    result = r.content.decode('utf-8')
    # string转dict并提取关键字
    print(json.loads(result)['data'])
    return json.loads(result)['data']


def text_to_speech(Sentence):
    engine = pyttsx3.init()
    engine.say(Sentence)
    engine.runAndWait()

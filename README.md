# Environment

- Python 3.67
- MacOS（以下环境配置方式均基于Mac系统，其他系统的配置方式可能会有一些不同）



# Speech to Text

使用了Python的语音识别库 [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

源码：https://github.com/Uberi/speech_recognition



## Installation

### SpeechRecognition

```python
pip install SpeechRecognition
```



### PyAudio

使用麦克风进行输入

主页：http://people.csail.mit.edu/hubert/pyaudio/

```python
# Mac上的安装方式

xcode-select --install	# 安装xcode, 已经装好的的话，执行的时候会提示

# 先用homebrew安装portaudio（pyaudio需要的库），否则会提示：'portaudio.h' file not found
brew remove portaudio	# 先用homebrew卸载
brew install portaudio	# 重新安装

sudo pip install pyaudio	# 安装pyaudio
```

Reference: https://stackoverflow.com/questions/33851379/pyaudio-installation-on-mac-python-3



### PocketSphinx

[CMU Sphinx](https://cmusphinx.github.io/) 是卡内基梅隆大学开发的开源语音识别引擎，可以离线工作，支持多种语言（包括中文）。

源码：https://github.com/cmusphinx



[PocketSphinx](https://pypi.org/project/pocketsphinx/) 是CMU Sphinx的Python封装接口。

源码：https://github.com/cmusphinx/pocketsphinx-python

```
pip install PocketSphinx
```



#### 添加中文语言包

查看 `SpeechRecognition` 包的安装路径（`'/path'`）：

```python
python -c "import speech_recognition as sr, os.path as p; print(p.dirname(sr.__file__))"
```

然后下载并解压 [Mandarin Chinese](https://drive.google.com/open?id=0Bw_EqP-hnaFNSWdqdm5maWZtTGc) 语言包，把 `zh-CN` 文件夹放入 `'/path/pocketsphinx-data'` 中



## Usage

### 获取音频

#### 从音频文件

```python
AUDIO_FILE = "chinese.flac"
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
```



#### 从麦克风

```python
# 从麦克风获取音频
with sr.Microphone() as source:
    # 校准环境噪声水平的energy threshold
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
```



#### 把音频写入文件

```python
# 写入 .wav
with open("speech.wav", "wb") as f:
    f.write(audio.get_wav_data())

# 写入 .flac .aiff .raw 等同理
```



#### 语音转文字

```python
import speech_recognition as sr

r = sr.Recognizer()

def speech_to_text():
    # CMU Sphinx
    try:
      	# languageType: 语种（中文：zh-CN，英文en-US）
        # audio: 音频
        return r.recognize_sphinx(audio, language = languageType)
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
```



# Text to Speech

使用了Python的文字转语音库 [pyttsx3](https://pypi.org/project/pyttsx3/)

源码：https://github.com/nateshmbhat/pyttsx3

文档：https://pyttsx3.readthedocs.io



## Installation

```python
pip install pyttsx3
pip install pyobjc # 依赖模块
```



## Usage

```python
import pyttsx3

def text_to_speech(Sentence):
    engine = pyttsx3.init()
    engine.say(Sentence)
    engine.runAndWait()
```
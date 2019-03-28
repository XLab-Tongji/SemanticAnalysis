# Environment

- Python 3.67
- MacOS（以下环境配置方式均基于Mac系统，其他系统的配置方式可能会有一些不同）



# Speech to Text

SpeechRecognition封装了录音、写入音频文件、录音在用户停止说话后自动停止的功能，但在自动停止录音的判断上不太灵敏。

但我自己写的录音还不如它…...所以还是直接用它来录音了…...



## 百度(在线)

在 https://cloud.baidu.com/product/speech 申请API。

文档：http://ai.baidu.com/docs#/ASR-API



### Configuration

安装Python包：

```python
pip install baidu-aip
```

Import：

```python
from aip import AipSpeech
```

填入APPID、API_KEY、SECRET_KEY：

```python
APP_ID = ""
API_KEY = ""
SECRET_KEY = ""
```

(也可以直接使用REST API：[demo](https://github.com/Baidu-AIP/speech-demo)



### Usage

```python
from TextSpeech import speech_to_text_baidu
speech_to_text_baidu()
```



## 科大讯飞(在线)

在 https://www.xfyun.cn/services/voicedictation 申请API。

文档：https://doc.xfyun.cn/rest_api/index.html



### Configuration

把APPID、API_KEY填到这里：

```python
URL = "http://api.xfyun.cn/v1/service/v1/iat"
APPID = ""
API_KEY = ""
```

要在讯飞管理面板中添加调用方api，否则会报错。



### Usage

```python
from TextSpeech import speech_to_text_ifly
speech_to_text_ifly()
```





## SpeechRecognition

使用了Python的语音识别库 [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

源码：https://github.com/Uberi/speech_recognition



### Configuration

#### SpeechRecognition

```python
pip install SpeechRecognition
```



#### PyAudio

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



#### PocketSphinx

[CMU Sphinx](https://cmusphinx.github.io/) 是卡内基梅隆大学开发的开源语音识别引擎，可以离线工作，支持多种语言（包括中文）。

源码：https://github.com/cmusphinx



[PocketSphinx](https://pypi.org/project/pocketsphinx/) 是CMU Sphinx的Python封装接口。

源码：https://github.com/cmusphinx/pocketsphinx-python

```
pip install PocketSphinx
```



**添加中文语言包：**

查看 `SpeechRecognition` 包的安装路径（`'/path'`）：

```python
python -c "import speech_recognition as sr, os.path as p; print(p.dirname(sr.__file__))"
```

然后下载并解压 [Mandarin Chinese](https://drive.google.com/open?id=0Bw_EqP-hnaFNSWdqdm5maWZtTGc) 语言包，把 `zh-CN` 文件夹放入 `'/path/pocketsphinx-data'` 中



### Usage

#### 语音转文字

```python
from TextSpeech import speech_to_text_cmu
speech_to_text_cmu()
```



#### 录音并写入文件

```python
from TextSpeech import record
record()
```





# Text to Speech

使用了Python的文字转语音库 [pyttsx3](https://pypi.org/project/pyttsx3/)

源码：https://github.com/nateshmbhat/pyttsx3

文档：https://pyttsx3.readthedocs.io



## Configuration

```python
pip install pyttsx3
pip install pyobjc # 依赖模块
```



## Usage

```python
from TextSpeech import text_to_speech
text_to_speech()
```


## 一、依赖安装

#### For speech recognition
```

pip install SpeechRecognition

pip install pyttsx3

pip install git+https://github.com/Baidu-AIP/python-sdk.git@master

pip install pyaudio 

pip install pydub
```

#### For speech emotion
```

pip install librosa

pip install speechpy
```
#### Others
tensorflow, torch, torchtext, warnings, ...

根据依赖缺失提示安装其余依赖

## 二、配置信息
配置信息写在config.py中

* READ_RESPONSE： AI端是否以语音交互
* INPUT： 用户端是否以语音交互
* EMOTION_RECOGNItION： 是否打开语音情绪识别功能
* GET_RADAR： 是否绘制雷达图

当前的默认配置为仅以文字形式交互，如需打开语音功能，设置READ_RESPONSE=True，INPUT=“voice”

## 三、启动方式
启动main.py

开启语音功能时建议使用耳机
## 一、依赖安装
以下依赖除特别指明，均安装默认版本：

#### 1. For speech recognition
```
pip install SpeechRecognition

pip install pyttsx3

pip install git+https://github.com/Baidu-AIP/python-sdk.git@master

pip install pyaudio 

pip install pydub
```

#### 2. For speech emotion
```
pip install librosa

pip install speechpy
```
#### 3. Others
tensorflow（1.13.1）, torch（0.4.1）, torchtext（0.3.1）, warnings, ...

根据依赖缺失提示安装其余依赖

torch安装方法参见官网安装教程： http://torch.ch/docs/getting-started.html#_

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

## 四、测试用例
引号部分为每轮人机对话中的用户输入部分。四个测试用例分别测试不同的场景。

1.在忙

```
“你说什么，我没听清”

“我现在不方便 以后再说吧”
```

2.拒绝

```
“你们是哪家银行的”

“好呀，你说”

“算了吧，我不感兴趣”
```

3.接受

```
“我没太听懂 你说什么活动”

“我要怎么做呢”

“存五万利息多少”

“好，我知道了”
```

4.检索

```
“你们公司叫什么”

“你们是不是骗子啊”

“你不会是机器人吧”

“好吧，你继续说”

“可以”
```
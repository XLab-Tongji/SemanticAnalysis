import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

from input import get_input
from AI.SemanticAnalysis import SemanticAnalysis
from AI.EmotionAnalysis import EmotionAnalysis
from config import Config
import jieba
import logging
jieba.setLogLevel(logging.INFO)
jieba.initialize()

config = Config()
# 载入或者训练模型
emotion = EmotionAnalysis(config)
ai = SemanticAnalysis(config)
sentence = get_input(config.INPUT)
while sentence:
    print("客户： " + sentence)
    # 分析情感
    emotion.analysis() #这里应该已经保存下客户语音了吧？
    ai.get_response(sentence)
    if ai.is_end():
        break
    sentence = get_input(config.INPUT)

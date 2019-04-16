import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
from config import Config
config = Config()
if config.EMOTION_RECOGNItION:
    import os
    import sys
    stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')
    import keras
    sys.stderr = stderr
import jieba
import logging
jieba.setLogLevel(logging.INFO)
jieba.initialize()
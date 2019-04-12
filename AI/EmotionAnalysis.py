import os.path as path
from Emotion.SER import load, test
from Emotion.Train import train

FILE_PATH = path.join(
    path.dirname(path.abspath(__file__)), "speech_tmp/speech.wav")


class EmotionAnalysis:
    def __init__(self, config):
        if config.TRAIN:
            self.model = train(config.EMOTION_MODEL)
        else:
            self.model = load(config.EMOTION_MODEL)
        self.model_name = config.EMOTION_MODEL
        self.get_radar = config.GET_RADAR

    def analysis(self):
        test(FILE_PATH, self.model_name, self.get_radar, self.model)

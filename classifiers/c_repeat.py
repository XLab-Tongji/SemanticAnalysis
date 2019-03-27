# may be a repetition classifier
from .classifier import Classifier


class C_repeat(Classifier):

    def __init__(self):
        self.classified = False
        self.wordsList = ['再说一下',
                          '再说下',
                          '再说一次',
                          '没听清',
                          '什么',
                          '听不清',
                          '再说一遍',
                          '什么呢']

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "repeat", "lastSentence"
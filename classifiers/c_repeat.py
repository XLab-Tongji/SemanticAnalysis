# may be a repetition classifier
from .classifier import Classifier


class C_repeat(Classifier):
    wordsList = ['什么','啥','再说']

    def __init__(self):
        self.classified = False

    # cfg_needed, intention, sub-intention
    def get_intention(self):

        return True, "repeat", "lastSentence"


# may be a repetition classifier
from .classifier import Classifier

class C_1_explanation(Classifier):

    def __init__(self):
        self.classified = False
        self.wordsList = ['干嘛','解释']

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        return True, "welcome", "explanation"

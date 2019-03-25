# may be a repetition classifier
from .classifier import Classifier

class C_1_explanation(Classifier):
    wordsList = ['干嘛','解释']

    def __init__(self):
        self.classified = False

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        return True, "welcome", "explanation"

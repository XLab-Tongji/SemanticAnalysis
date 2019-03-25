# may be a s1 success classifier
from .classifier import Classifier

class C_1_success(Classifier):
    wordsList = ['好','嗯','可以','方便']
    nextState = 1

    def __init__(self):
        self.classified = False

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        return True, "introduction", "introduction"

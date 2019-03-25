# may be a repetition classifier
from .classifier import Classifier

class C_file(Classifier):
    wordsList = ['不要','再见']
    nextState = -1

    def __init__(self):
        self.classified = False

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        return True, "decline", "fail"


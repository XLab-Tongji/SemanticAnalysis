# may be a repetition classifier
from .classifier import Classifier

class C_decline(Classifier):

    def __init__(self):
        self.classified = False
        self.wordsList = ['不要','再见']
        self.nextState = self.END

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        return True, "end", "decline"
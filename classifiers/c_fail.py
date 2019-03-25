# may be a repetition classifier
from .classifier import Classifier

class C_decline(Classifier):
    wordsList = ['不要','再见']

    def __init__(self):
        self.classified = False

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        return True, "end", "decline"


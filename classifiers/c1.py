# may be a repetition classifier
from .classifier import Classifier

class C1(Classifier):
    def __init__(self):
        self.classified = True

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        return True, "welcome", "explanation"


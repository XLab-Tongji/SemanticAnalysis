# may be a s1 success classifier
from .classifier import Classifier

class C_2_success(Classifier):
    def __init__(self):
        self.classified = False
        self.wordsList = ['好','嗯','可以']
        self.nextState = self.END

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "end", "success"

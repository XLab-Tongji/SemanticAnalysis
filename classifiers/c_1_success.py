# may be a s1 success classifier
from .classifier import Classifier

class C_1_success(Classifier):

    def __init__(self):
        self.classified = False
        self.wordsList = ['好','嗯','可以','方便']
        self.nextState = self.INTRODUCTION

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        return True, "introduction", "introduction"

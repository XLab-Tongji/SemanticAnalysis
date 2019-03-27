# may be a unidentified classifier
from .classifier import Classifier
from configparser import ConfigParser

class C_unidentified(Classifier):

    def __init__(self):
        self.times = 0
        self.classified = True

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.times += 1
        if self.times == 2:
            return True, "unidentified", "twice"
        else:
            if self.times == 3:
                return True, "end", "unidentified"
        return True, "unidentified", "once"

    def doClassification(self,sentence):
        for word in self.wordsList:
            if word in sentence:
                self.classified = True
                break
        if self.times == 2:
            self.nextState = 2
        return self.nextState

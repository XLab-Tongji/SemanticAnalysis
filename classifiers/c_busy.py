# may be a repetition classifier
from .classifier import Classifier

class C_busy(Classifier):

    def __init__(self):
        self.classified = False
        self.nextState = self.END
        self.wordsList = ['在开会',
                          '在开车',
                          '回头给我打电话',
                          '没有时间',
                          '不方便',
                          '改天打吧',
                          '换个时间打吧']

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "end", "busy"


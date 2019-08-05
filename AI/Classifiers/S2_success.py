# may be a s1 success classifier
from .classifier import Classifier

class S2Success(Classifier):
    def __init__(self):
        self.classified = False
        self.words_list = ['嗯',
                           '行',
                           '有',
                           '要',
                           '需要',
                           '好',
                           '可以']
        self.next_state = self.END

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "end", "success"

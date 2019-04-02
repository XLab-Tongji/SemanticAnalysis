# may be a s1 success classifier
from .classifier import Classifier

class S1Success(Classifier):
    def __init__(self):
        self.classified = False
        self.next_state = self.INTRODUCTION
        self.words_list = ['嗯',
                           '行',
                           '有',
                           '要',
                           '需要',
                           '好',
                           '我要',
                           '可以',
                           '有的',
                           '怎么弄',
                           '怎么做',
                           '操作',
                           '好做',
                           '好弄',
                           '麻烦吗',
                           '快吗',
                           '方便',
                           '你说说看']

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "introduction", "introduction"

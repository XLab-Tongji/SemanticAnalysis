# may be a s1 success classifier
from .classifier import Classifier

class C_1_success(Classifier):

    def __init__(self):
        self.classified = False
        self.nextState = self.INTRODUCTION
        self.wordsList = ['嗯',
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
                          '现在方便',
                          '你说说看']

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "introduction", "introduction"

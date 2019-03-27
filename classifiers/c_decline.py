# may be a repetition classifier
from .classifier import Classifier

class C_decline(Classifier):

    def __init__(self):
        self.classified = False
        self.nextState = self.END
        self.wordsList = ['不用',
                          '你们烦死了',
                          '不感兴趣',
                          '没兴趣',
                          '不要',
                          '没时间',
                          '不要再给我打电话了',
                          '没有钱做理财',
                          '骗子',
                          '不方便',
                          '我有事',
                          '在上班',
                          '在公司',
                          '银行太远',
                          '没需求']

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "end", "decline"
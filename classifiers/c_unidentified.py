# may be a unidentified classifier
from .classifier import Classifier
from SemanticAnalysis import SemanticAnalysis
from configparser import ConfigParser

class C_unidentified(Classifier):
    def __init__(self):
        a = SemanticAnalysis.INITIAL
        self.cfgParser = ConfigParser()
        self.cfgParser.read("intention.cfg", encoding="UTF8")
        self.classified = True

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        sentence = self.cfgParser['repeat']['lastSentence']
        print(sentence)
        print(self.cfgParser['unidentified']['once'])
        ###由于此处打开的cfg文件与ai的cfg不是同一个对象，故无法通过查询上一条输出判断是否进行第二、第三次未识别的回应
        if sentence == self.cfgParser['unidentified']['once']:
            return True, "unidentified", "twice"
        else:
            if sentence == self.cfgParser['unidentified']['twice']:
                return True, "decline", "unidentified"
        return True, "unidentified", "once"


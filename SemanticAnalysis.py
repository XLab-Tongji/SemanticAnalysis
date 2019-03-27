from configparser import ConfigParser

from classifiers.c_1_success import C_1_success
from classifiers.c_2_success import C_2_success

from classifiers.c_chat_company import C_chat_company
from classifiers.c_decline import C_decline
from classifiers.c_repeat import C_repeat
from classifiers.c_unidentified import C_unidentified
from classifiers.c_busy import C_busy

class SemanticAnalysis:
    # state set
    UNCHANGED = -1
    INITIAL = 0
    INTRODUCTION = 1
    END = 2

    #classifiers initial
    cUnidentified = C_unidentified()
    cChat = C_chat_company()
    cDecline = C_decline()
    cRepeat = C_repeat()
    cBusy = C_busy()

    def __init__(self):
        self.state = SemanticAnalysis.INITIAL
        self.cfgParser = ConfigParser()
        self.cfgParser.read("intention.cfg", encoding="UTF8")

        introduction = self._response_from_config("welcome", "prologue")
        print(introduction)

    def get_response(self, sentence):
        classifiers = []
        if self.state == SemanticAnalysis.INITIAL:
            classifiers.append(C_1_success())
            classifiers.append(self.cChat)
            classifiers.append(self.cRepeat)
            classifiers.append(self.cDecline)
            classifiers.append(self.cUnidentified)

        if self.state == SemanticAnalysis.INTRODUCTION:
            classifiers.clear()
            classifiers.append(C_2_success())
            classifiers.append(self.cChat)
            classifiers.append(self.cRepeat)
            classifiers.append(self.cDecline)
            classifiers.append(self.cUnidentified)

        cfg_needed = False
        intention, subintention = None, None

        for classifier in classifiers:
            # do classification...
            nextState = classifier.doClassification(sentence)

            if classifier.is_classified():
                cfg_needed, intention, subintention = classifier.get_intention()

                # 状态转换：INSTALL->INTRUDUCTION->END
                if nextState != SemanticAnalysis.UNCHANGED:
                    self.state = nextState
                break

        ret = None
        if cfg_needed:
            ret = self._response_from_config(intention, subintention)
            self._write_to_config(ret)
        return ret

    def is_end(self):
        return self.state == SemanticAnalysis.END

    def _response_from_config(self, intention, subintention):
        try:
            sentence = self.cfgParser[intention][subintention]
            return sentence
        except KeyError:
            print("\nERROR! : Missing configuration for {} and {}\n".format(intention, subintention))

    def _write_to_config(self,sentence):
        try:
            self.cfgParser['repeat']['lastSentence'] = sentence

            #未识别情况计数器
            if sentence != self.cfgParser['unidentified']['once']:
                if sentence != self.cfgParser['unidentified']['twice']:
                    self.cUnidentified.times = 0
        finally:
            return
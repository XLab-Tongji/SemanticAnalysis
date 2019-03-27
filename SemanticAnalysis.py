from configparser import ConfigParser

from classifiers.S1_success import S1_Success
from classifiers.S2_success import S2_Success

from classifiers.chatting import Chatting
from classifiers.decline import Decline
from classifiers.repeat import Repeat
from classifiers.unidentified import Unidentified
from classifiers.busy import C_busy

class SemanticAnalysis:
    # state set
    UNCHANGED = -1
    INITIAL = 0
    INTRODUCTION = 1
    END = 2

    def __init__(self):
        self.state = SemanticAnalysis.INITIAL
        self.cfgParser = ConfigParser()
        self.cfgParser.read("intention.cfg", encoding="UTF8")

        # classifiers initial
        self.cUnidentified = Unidentified()
        self.cChat = Chatting()
        self.cDecline = Decline()
        self.cRepeat = Repeat()
        self.cBusy = C_busy()

        introduction = self._response_from_config("welcome", "prologue")
        print(introduction)

    def get_response(self, sentence):
        classifiers = []
        if self.state == SemanticAnalysis.INITIAL:
            classifiers.append(S1_Success())
            classifiers.append(self.cChat)
            classifiers.append(self.cRepeat)
            classifiers.append(self.cDecline)
            classifiers.append(self.cUnidentified)
        elif self.state == SemanticAnalysis.INTRODUCTION:
            classifiers.append(S2_Success())
            classifiers.append(self.cChat)
            classifiers.append(self.cRepeat)
            classifiers.append(self.cDecline)
            classifiers.append(self.cUnidentified)

        cfg_needed = False
        intention, sub_intention = None, None

        for classifier in classifiers:
            # do classification...
            next_state = classifier.do_classification(sentence)

            if classifier.is_classified():
                cfg_needed, intention, sub_intention = classifier.get_intention()

                # 状态转换：INSTALL->INTRODUCTION->END
                if next_state != SemanticAnalysis.UNCHANGED:
                    self.state = next_state
                break

        ret = None
        if cfg_needed:
            ret = self._response_from_config(intention, sub_intention)
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

    def _write_to_config(self, sentence):
        try:
            self.cfgParser['repeat']['lastSentence'] = sentence

            # 未识别情况计数器
            if sentence != self.cfgParser['unidentified']['once']:
                if sentence != self.cfgParser['unidentified']['twice']:
                    self.cUnidentified.times = 0
        finally:
            return

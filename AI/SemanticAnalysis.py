from configparser import ConfigParser
from .TextSpeech import text_to_speech
from .Classifiers import *
import os.path as path

class SemanticAnalysis:
    # state set
    UNCHANGED = -1
    INITIAL = 0
    INTRODUCTION = 1
    END = 2

    def __init__(self, config):
        self.state = SemanticAnalysis.INITIAL
        self.cfg_parser = ConfigParser()
        self.cfg_parser.read(path.join(path.dirname(path.abspath(__file__)), "intention.cfg"), encoding="UTF8")

        # classifiers initial
        self.c_unidentified = Unidentified()
        self.c_chat = Chatting()
        self.c_decline = Decline()
        self.c_repeat = Repeat()
        self.c_busy = Busy()

        # basic config
        self.READ_RESPONSE = config.READ_RESPONSE

        introduction = self._response_from_config("welcome", "prologue")
        self._output_response(introduction)

    def _output_response(self, response):
        print("客服: " + response)
        if self.READ_RESPONSE:
            text_to_speech(response)

    def get_response(self, sentence):
        classifiers = []
        if self.state == SemanticAnalysis.INITIAL:
            classifiers.append(S1Success())
            classifiers.append(self.c_chat)
            classifiers.append(self.c_repeat)
            classifiers.append(self.c_decline)
            classifiers.append(self.c_unidentified)
        elif self.state == SemanticAnalysis.INTRODUCTION:
            classifiers.append(S2Success())
            classifiers.append(self.c_chat)
            classifiers.append(self.c_repeat)
            classifiers.append(self.c_decline)
            classifiers.append(self.c_unidentified)

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

        response = None
        if cfg_needed:
            response = self._response_from_config(intention, sub_intention)
            self._write_to_config(response)
        self._output_response(response)

    def is_end(self):
        return self.state == SemanticAnalysis.END

    def _response_from_config(self, intention, sub_intention):
        try:
            sentence = self.cfg_parser[intention][sub_intention]
            return sentence
        except KeyError:
            print("\nERROR! : Missing configuration for {} and {}\n".format(intention, sub_intention))

    def _write_to_config(self, sentence):
        try:
            self.cfg_parser['repeat']['lastSentence'] = sentence

            # 未识别情况计数器
            if sentence != self.cfg_parser['unidentified']['once']:
                if sentence != self.cfg_parser['unidentified']['twice']:
                    self.c_unidentified.times = 0
        finally:
            return

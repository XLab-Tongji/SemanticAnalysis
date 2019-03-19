from configparser import ConfigParser
from classifiers.classifier import Classifier
from classifiers.c1 import C1
from classifiers.c2 import C2

class SemanticAnalysis:
    # state set
    INITIAL = 0
    INTRODUCTION = 1
    END = 2

    def __init__(self):
        self.state = SemanticAnalysis.INITIAL
        self.cfgParser = ConfigParser()
        self.cfgParser.read("intention.cfg", encoding="UTF8")

        introduction = self._response_from_config("welcome", "introduction")
        print(introduction)

    def get_response(self, sentence):
        classifiers = []
        if self.state == SemanticAnalysis.INITIAL:
            classifiers.append(C1())
            classifiers.append(C2())
        cfg_needed = False
        intention, subintention = None, None
        for classifier in classifiers:
            # do classification...
            if classifier.is_classified():
                cfg_needed, intention, subintention = classifier.get_intention()
                break

        ret = None
        if cfg_needed:
            ret = self._response_from_config(intention, subintention)
        return ret

    def is_end(self):
        return self.state == SemanticAnalysis.END

    def _response_from_config(self, intention, subintention):
        try:
            sentence = self.cfgParser[intention][subintention]
            return sentence
        except KeyError:
            print("\nERROR! : Missing configuration for {} and {}\n".format(intention, subintention))


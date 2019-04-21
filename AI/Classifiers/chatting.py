# may be a repetition classifier
from .classifier import Classifier
from makeVec import  Matcher

class Chatting(Classifier):
    def __init__(self):
        self.classified = False
        self.words_list = ['公司', '哪家']
        self.reply = 'none'

    def get_intention(self):
        self.classified = False
        return True, "chat", self.reply[1]

    def do_classification(self, sentence):
        matcher = Matcher()
        self.reply = matcher.simi_answermap_vec(sentence)
        if self.reply[1] != 'none':
            self.classified = True
        return self.next_state
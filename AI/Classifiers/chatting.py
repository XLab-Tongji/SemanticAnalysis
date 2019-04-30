# may be a repetition classifier
from .classifier import Classifier
from makeVec import  Matcher

class Chatting(Classifier):
    def __init__(self):
        self.classified = False
        self.words_list = ['公司', '哪家']
        self.reply = 'none'
        self.set_to_state2 = ['11','4','12','13','17','20','21','23','24','26','28','29','30','32']
        self.set_to_end = ['34']
        self.matcher = Matcher()
        self.matcher.make_vec_file()

    def get_intention(self):
        self.classified = False
        return True, "chat", self.reply[1]

    def do_classification(self, sentence):
        self.reply = self.matcher.simi_answermap_vec(sentence)
        k = self.reply[1]
        if k != 'none':
            self.classified = True
            for s in self.set_to_state2:
                if k == s:
                    self.next_state = 1
            for s_ in self.set_to_end:
                if k == s_:
                    self.next_state = 2
        return self.next_state
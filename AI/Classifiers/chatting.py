# may be a repetition classifier
from .classifier import Classifier

class Chatting(Classifier):
    def __init__(self):
        self.classified = False
        self.words_list = ['公司', '哪家']

    def get_intention(self):
        self.classified = False
        return True, "normalQuestion", "yourCompany?"

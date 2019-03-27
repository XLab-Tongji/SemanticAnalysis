# may be a repetition classifier
from .classifier import Classifier

class C_chat_company(Classifier):

    def __init__(self):
        self.classified = False
        self.wordsList = ['公司', '哪家']

    def get_intention(self):
        self.classified = False
        return True, "normalQuestion" , "yourcompany?"
# may be a repetition classifier
from .classifier import Classifier

class C_chat_company(Classifier):
    wordsList = ['公司','哪家']
    nextState = -1

    def __init__(self):
        self.classified = False

    def get_intention(self):
        return True, "normalQuestion" , "yourcompany?"
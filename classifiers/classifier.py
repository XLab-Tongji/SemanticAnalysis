class Classifier:
    wordsList = []
    nextState = 0

    def __init__(self):
        self.classified = False
        return

    def is_classified(self):
        return self.classified

    def get_intention(self):
        raise NotImplementedError

    def doClassification(self,sentence):
        for word in self.wordsList:
            if word in sentence:
                self.classified = True
                break
        return self.nextState
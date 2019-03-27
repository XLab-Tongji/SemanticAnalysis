class Classifier:
    wordsList = []

    INITIAL = 0
    INTRODUCTION = 1
    END = 2
    UNCHANGED = -1

    nextState = UNCHANGED

    def __init__(self):
        self.classified = False
        self.nextState = self.UNCHANGED
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
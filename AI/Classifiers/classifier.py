class Classifier:
    words_list = []

    INITIAL = 0
    INTRODUCTION = 1
    END = 2
    UNCHANGED = -1

    next_state = UNCHANGED

    def __init__(self):
        self.classified = False
        self.next_state = self.UNCHANGED
        return

    def is_classified(self):
        return self.classified

    def get_intention(self):
        raise NotImplementedError

    def do_classification(self, sentence):
        for word in self.words_list:
            if word in sentence:
                self.classified = True
                break
        return self.next_state

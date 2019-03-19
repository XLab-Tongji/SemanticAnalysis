class Classifier:
    def __init__(self):
        self.classified = False
        return

    def is_classified(self):
        return self.classified

    def get_intention(self):
        raise NotImplementedError

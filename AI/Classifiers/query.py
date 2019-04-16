# may be a repetition classifier
from .classifier import Classifier
from .models.load import predict, load_data, load_model

class Query(Classifier):
    def __init__(self, config):
        self.config = config
        self.classified = False
        self.next_state = self.QUERIED
        self.words_list = ['什么',
                           '再讲一遍']
        self.text_field, self.label_field = load_data(target="0", config=config)
        self.model = load_model("FastText", "request.pt", self.text_field, config)

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "welcome", "explanation"


    def do_classification(self, sentence):
        if self.config.USE_MODEL:
            self.classified = predict(self.model, self.text_field, self.label_field, sentence, self.config)
            return self.next_state
        else:
            super().do_classification(sentence)

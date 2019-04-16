# may be a repetition classifier
from .classifier import Classifier
from .models.load import predict, load_data, load_model

class Decline(Classifier):
    def __init__(self, config):
        self.config = config
        self.classified = False
        self.next_state = self.END
        self.words_list = ['不用',
                           '不需要',
                           '你们烦死了',
                           '不感兴趣',
                           '没兴趣',
                           '不要',
                           '没时间',
                           '不要再给我打电话了',
                           '没有钱做理财',
                           '骗子',
                           '不方便',
                           '我有事',
                           '在上班',
                           '在公司',
                           '银行太远',
                           '没需求']
        self.text_field, self.label_field = load_data(target="6", config=config)
        self.model = load_model("FastText", "refuse.pt", self.text_field, config)

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "end", "decline"

    def do_classification(self, sentence):

        if self.config.USE_MODEL:
            self.classified = predict(self.model, self.text_field, self.label_field, sentence, self.config)
            return self.next_state
        else:
            super().do_classification(sentence)

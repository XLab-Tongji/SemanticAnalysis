# may be a repetition classifier
from .classifier import Classifier
from .models.load import predict, load_data, load_model

class Busy(Classifier):
    def __init__(self, config):
        self.config = config
        self.classified = False
        self.next_state = self.END
        self.words_list = ['在开会',
                           '在开车',
                           '回头给我打电话',
                           '没有时间',
                           '不方便',
                           '改天打吧',
                           '换个时间打吧']
        self.text_field, self.label_field = load_data(target="5", config=config)
        self.model = load_model("FastText", "busy.pt", self.text_field, config)

    # cfg_needed, intention, sub-intention
    def get_intention(self):
        self.classified = False
        return True, "end", "busy"

    def do_classification(self, sentence):
        if self.config.USE_MODEL:
            self.classified = predict(self.model, self.text_field, self.label_field, sentence, self.config)
            return self.next_state
        else:
            super().do_classification(sentence)


import torchtext.data as data
import random
import os.path as path

class Dataset(data.Dataset):
    def __init__(self, pos_label, text_field, label_field, examples=None):
        def clean(string):
            return string

        text_field.preprocessing = data.Pipeline(clean)
        fields = [("text", text_field), ("label", label_field)]
        self.index = -1
        flag = False
        if examples is None:
            file_name = path.join(path.dirname(path.abspath(__file__)), "total.csv")
            with open(file_name, encoding="UTF8") as f:
                examples = []
                for line in f:
                    sentence, label = line.strip().rsplit(",", 1)
                    if label == pos_label:
                        label = "0"
                    else:
                        label = "1"
                        if not flag:
                            self.index = len(examples) - 1
                            flag = True
                    examples.append(data.Example.fromlist([sentence, label], fields))
        super(Dataset, self).__init__(examples, fields)

    @classmethod
    def split(cls, pos_label, text_field, label_field, config):
        dataset = cls(pos_label, text_field, label_field)
        index = dataset.index
        examples = dataset.examples
        if hasattr(config, "SHUFFLE") and config.SHUFFLE: random.shuffle(examples)
        length = len(examples)
        test_size = int((0.1 / 2) * length)
        train_examples = examples[: index - test_size].__add__(examples[: length - test_size])
        test_examples = examples[index - test_size: index].__add__(examples[length - test_size: length])
        return (cls(pos_label, text_field, label_field, examples=train_examples),
                cls(pos_label, text_field, label_field, examples=test_examples))

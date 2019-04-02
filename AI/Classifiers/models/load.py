import os
import torch
import torch.nn.functional as F
import datetime
import torch.autograd as autograd
import jieba.posseg as pseg
from .fasttext import FastText
import torchtext.data as data
from .input import Dataset
from torchtext.vocab import Vectors
import os.path as path

def _chinese_tokenizer(sentence):
    exclusion = ["e", "x", "y"]  # e 叹词  x 非语素词  y 语气词
    return [word for (word, flag) in pseg.cut(sentence) if flag not in exclusion]

def load_data(target, config):
    text_field = data.Field(tokenize=_chinese_tokenizer)
    label_field = data.Field(sequential=False)

    train_data, test_data = Dataset.split(target, text_field, label_field, config)
    embedding = path.join(path.dirname(path.abspath(__file__)), config.PRETRAINED_EMBEDDING)
    cache = path.join(path.dirname(path.abspath(__file__)), ".vector_cache/")
    weights = Vectors(name=embedding, cache=cache)

    text_field.build_vocab([{key: 1} for key in weights.itos], vectors=weights)
    label_field.build_vocab(train_data)

    config.EMBED_NUM = len(text_field.vocab)
    config.EMBED_DIM = len(weights.vectors[0])
    config.CLASS_NUM = len(label_field.vocab) - 1
    return text_field, label_field

def load_model(model_name, ckpt, text_field, config):
    model = None
    if model_name == "FastText":
        model = FastText(config, text_field.vocab.vectors)
    if config.CUDA:
        torch.cuda.set_device(config.DEVICE)
        model = model.cuda()
    device = config.DEVICE if config.CUDA else "cpu"
    model.load_state_dict(torch.load(path.join(path.dirname(path.abspath(__file__)), ckpt), map_location=device))
    return model

def predict(model, text_field, label_field, sentence, config):
    model.eval()
    sentence = text_field.preprocess(sentence)
    # while len(sentence) < 3:
    #     sentence.append("<pad>")
    sentence = [[text_field.vocab.stoi[x] for x in sentence]]
    x = torch.tensor(sentence)
    x = autograd.Variable(x)
    if config.CUDA:
        x = x.cuda()
    output = model(x)
    _, pred = torch.max(output, 1)
    return label_field.vocab.itos[pred.data[0]+1] == "0"

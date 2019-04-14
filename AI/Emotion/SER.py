import numpy as np

from .Utilities import get_feature
from .Utilities import get_feature_svm
from .Utilities import load_model
from .Utilities import Radar

DATA_PATH = 'DataSet/Berlin'
# CLASS_LABELS = ("Angry", "Happy", "Neutral", "Sad")

CLASS_LABELS = ("Angry", "Fearful", "Happy", "Neutral", "Sad", "Surprise")
# CLASS_LABELS = ("angry", "fear", "happy", "neutral", "sad", "surprise")


def load(model_name="SVM"):
    if model_name == "LSTM" or model_name == "CNN":
        model = load_model(model_name=model_name, load_model="DNN")
    elif model_name == "SVM" or model_name == "MLP":
        model = load_model(model_name=model_name, load_model="ML")
    else:
        print("情感识别模型选择有误")

    return model


def test(file_path: str, model_name="SVM", get_radar=False, model=None):
    if model_name == "LSTM":
        LSTM(file_path, get_radar, model)
    elif model_name == "CNN":
        CNN(file_path, get_radar, model)
    elif model_name == "SVM":
        SVM(file_path, get_radar, model)
    elif model_name == "MLP":
        MLP(file_path, get_radar, model)
    else:
        print("情感识别模型选择有误")


def LSTM(file_path: str, get_radar=False, model=None):
    if model is None:
        print("情感识别模型载入出错")
        return
    NUM_LABELS = len(CLASS_LABELS)
    result = np.argmax(model.predict(np.array([get_feature(file_path)])))
    result_prob = model.predict(np.array([get_feature(file_path)]))[0]
    _print_result(result, result_prob)
    if get_radar:
        Radar(result_prob, CLASS_LABELS, NUM_LABELS)


def CNN(file_path: str, get_radar=False, model=None):
    if model is None:
        print("情感识别模型载入出错")
        return

    FLATTEN = False
    test = np.array([get_feature(file_path, flatten=FLATTEN)])
    in_shape = test[0].shape
    test = test.reshape(test.shape[0], in_shape[0], in_shape[1], 1)
    print('Recogntion: ', CLASS_LABELS[np.argmax(model.predict(test))])


def MLP(file_path: str, get_radar=False, model=None):
    if model is None:
        print("情感识别模型载入出错")
        return
    FLATTEN = True
    NUM_LABELS = len(CLASS_LABELS)

    result = model.predict(np.array([get_feature(file_path, flatten=FLATTEN)]))
    result_prob = model.predict_proba(
        np.array([get_feature(file_path, flatten=FLATTEN)]))
    _print_result(result, result_prob)
    if get_radar:
        Radar(result_prob, CLASS_LABELS, NUM_LABELS)


def SVM(file_path: str, get_radar=False, model=None):
    if model is None:
        print("情感识别模型载入出错")
        return
    NUM_LABELS = len(CLASS_LABELS)

    result = model.predict(np.array([get_feature_svm(file_path, mfcc_len=48)]))
    result_prob = model.predict_proba(
        np.array([get_feature_svm(file_path, mfcc_len=48)]))[0]
    _print_result(result, result_prob)
    if get_radar:
        Radar(result_prob, CLASS_LABELS, NUM_LABELS)

def _print_result(result, result_prob):
    print('Recogntion: ', CLASS_LABELS[result[0] - 1])
    print('Probability: ', result_prob)
# SVM("test.wav")

DATA_PATH = 'DataSet/Berlin'
CLASS_LABELS = ("Angry", "Happy", "Neutral", "Sad")

# CLASS_LABELS = ("Angry", "Fearful", "Happy", "Neutral", "Sad", "Surprise")
# CLASS_LABELS = ("angry", "fear", "happy", "neutral", "sad", "surprise")


def train(model_name="SVM"):
    if model_name == "SVM":
        train_SVM()
    elif model_name == "LSTM":
        train_LSTM()
    elif model_name == "CNN":
        train_CNN()
    elif model_name == "MLP":
        train_MLP()
    else:
        print("情感识别模型选择有误")


def train_LSTM():
    from keras.utils import np_utils
    from .DNN_Model import LSTM_Model
    from .Utilities import get_data
    FLATTEN = False
    NUM_LABELS = len(CLASS_LABELS)
    SVM = False

    x_train, x_test, y_train, y_test = get_data(
        DATA_PATH, class_labels=CLASS_LABELS, flatten=FLATTEN, _svm=SVM)
    y_train = np_utils.to_categorical(y_train)
    y_test_train = np_utils.to_categorical(y_test)

    print(
        '-------------------------------- LSTM Train Start --------------------------------'
    )
    model = LSTM_Model(input_shape=x_train[0].shape, num_classes=NUM_LABELS)
    model.train(x_train, y_train, x_test, y_test_train, n_epochs=50)
    model.evaluate(x_test, y_test)
    model.save_model("LSTM")

    print(
        '--------------------------------- LSTM Train End ---------------------------------'
    )


def train_CNN():
    from .DNN_Model import CNN_Model
    from keras.utils import np_utils
    from .Utilities import get_data
    FLATTEN = False
    NUM_LABELS = len(CLASS_LABELS)
    SVM = False

    x_train, x_test, y_train, y_test = get_data(
        DATA_PATH, class_labels=CLASS_LABELS, flatten=FLATTEN, _svm=SVM)
    y_train = np_utils.to_categorical(y_train)
    y_test_train = np_utils.to_categorical(y_test)
    in_shape = x_train[0].shape
    x_train = x_train.reshape(x_train.shape[0], in_shape[0], in_shape[1], 1)
    x_test = x_test.reshape(x_test.shape[0], in_shape[0], in_shape[1], 1)

    print(
        '-------------------------------- CNN Train Start --------------------------------'
    )
    model = CNN_Model(input_shape=x_train[0].shape, num_classes=NUM_LABELS)
    model.train(x_train, y_train, x_test, y_test_train, n_epochs=1)
    model.evaluate(x_test, y_test)
    model.save_model("CNN")
    print(
        '-------------------------------- CNN Train End --------------------------------'
    )


def train_MLP():
    from .ML_Model import MLP_Model
    from .Utilities import get_data
    FLATTEN = True
    SVM = False

    x_train, x_test, y_train, y_test = get_data(
        DATA_PATH, class_labels=CLASS_LABELS, flatten=FLATTEN, _svm=SVM)
    model = MLP_Model()  # 要用的方法（SVM / MLP）
    print(
        '-------------------------------- MLP Train Start --------------------------------'
    )
    model.train(x_train, y_train)
    model.evaluate(x_test, y_test)
    model.save_model("MLP")

    print(
        '---------------------------------- MLP Train End ----------------------------------'
    )


def train_SVM():
    from .ML_Model import SVM_Model
    from .Utilities import get_data

    FLATTEN = True
    SVM = True

    x_train, x_test, y_train, y_test = get_data(
        DATA_PATH,
        mfcc_len=48,
        class_labels=CLASS_LABELS,
        flatten=FLATTEN,
        _svm=SVM)
    model = SVM_Model()
    print(
        '-------------------------------- SVM Train Start --------------------------------'
    )
    model.train(x_train, y_train)
    model.save_model("SVM")
    print(
        '---------------------------------- SVM Train End ----------------------------------'
    )

class Config:
    READ_RESPONSE = False
    INPUT = "command"  # voice, command

    USE_MODEL = True
    PRETRAINED = True
    PRETRAINED_EMBEDDING = "embeddings/sgns.weibo.bigram-char"
    CUDA = False
    DEVICE = 0

    EMOTION_RECOGNItION = True
    EMOTION_MODEL = "SVM"  # SVM, CNN, LSTM, MLP
    GET_RADAR = True
    TRAIN = False
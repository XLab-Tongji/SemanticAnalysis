class Config:
    READ_RESPONSE = False
    INPUT = "command"  # voice, command

    USE_MODEL = True
    PRETRAINED = True
    PRETRAINED_EMBEDDING = "embeddings/sgns.weibo.bigram"
    CUDA = False
    DEVICE = 0

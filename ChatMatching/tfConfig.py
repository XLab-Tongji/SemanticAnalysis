from configparser import ConfigParser
class TfConfig:
    ex_stop_words = True
    ex_idf = False
    ex_dict = True
    answermap_path = "ChatMatching/extra/answerMap.ini"
    cfg_path = "ChatMatching/extra/config.ini"
    stop_path = "ChatMatching/extra/myStop.txt"
    idf_path = "ChatMatching/extra/myIDF.txt"
    dict_path = "ChatMatching/extra/myDict.dict"
    words_path = "ChatMatching/extra/myWordsLib.txt"

    TRAIN = True
    TEST = False
    mode = TRAIN
    make_idf = True
    rewrite_vec = mode

    def __init__(self):
        self.cfgparser = ConfigParser()
        self.cfgparser.read(self.cfg_path, encoding="UTF8")
        self.threshold = float(self.cfgparser.get('parameters', 'threshold'))

    def set_threshold(self, v):
        self.cfgparser.set('parameters', 'threshold', str(v))
        with open('extra/config.ini', 'w+') as fw:
            self.cfgparser.write(fw)
        self.threshold = v
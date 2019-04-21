import jieba
import jieba.analyse
from utility import Utility as Ut
from configparser import ConfigParser
from tfConfig import TfConfig
import numpy
import json


class Matcher:
    def __init__(self):
        self.cfg = TfConfig()
        if self.cfg.ex_stop_words:
            jieba.analyse.set_stop_words(TfConfig.stop_path)
        if self.cfg.ex_idf:
            jieba.analyse.set_idf_path(TfConfig.idf_path)
        if self.cfg.ex_dict:
            jieba.load_userdict(TfConfig.dict_path)
        self.cfgParser = ConfigParser()
        self.cfgParser.read(self.cfg.answermap_path, encoding="UTF8")
        self.index = ['1', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', '11', '12',
                      '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24',
                      '25', '26', '27', '28', '29', '30',
                      '30', '31', '32', '33', '34']

    def show(self,content: str):
        seg_list = jieba.cut(content)
        print(", ".join(seg_list))
        for x, w in jieba.analyse.extract_tags(content,withWeight = True):
            print('%s,%s' %(x, w))

    def make_vec(self,content:str):
        vec=[]
        words = Ut.file2List(TfConfig.words_path)
        seg_list = jieba.analyse.extract_tags(content, withWeight=True)
        for word in words:
            v = 0
            for x, w in seg_list:
                if x == word:
                    v = w
            vec.append(v)
        return vec

    def simi_strs(self, s1, s2):
        v1 = self.make_vec(s1)
        v2 = self.make_vec(s2)
        result = self.simi_vecs(v1, v2)
        return result

    def simi_vecs(self, v1, v2):
        result = 0.0
        s1_cut_code = numpy.array(v1)
        s2_cut_code = numpy.array(v2)
        if (numpy.linalg.norm(s1_cut_code) != 0.0) & (numpy.linalg.norm(s2_cut_code) != 0.0):
            result = s1_cut_code.dot(s2_cut_code) / (numpy.sqrt(s1_cut_code.dot(s1_cut_code)) * numpy.sqrt(s2_cut_code.dot(s2_cut_code)))
        return result

    def simi_answermap(self, s1):
        threshold = self.cfg.threshold
        target = 'none'
        answer = 'none'
        best_value = 0
        for i in self.index:
            s2 = self.cfgParser[i]['question']
            result = self.simi_strs(s1, s2)
            if result > threshold and result>best_value:
                best_value = result
                answer = self.cfgParser[i]['answer']
                target = i
        return [best_value, target, answer]

    def simi_answermap_vec(self, s1):
        v1 = self.make_vec(s1)
        threshold = self.cfg.threshold
        target = 'none'
        answer = 'none'
        best_value = 0
        for i in self.index:
            v2 = json.loads(self.cfgParser[i]['vector'])
            result = self.simi_vecs(v1, v2)
            if result > threshold and result > best_value:
                best_value = result
                answer = self.cfgParser[i]['answer']
                target = i
        return [best_value, target, answer]
        # return answer

    def make_vec_file(self):
        for i in self.index:
            vec = self.make_vec(self.cfgParser[i]['question'])
            self.cfgParser[i]['vector'] = str(vec)
        with open(self.cfg.answermap_path, 'w+') as fw:
            self.cfgParser.write(fw)
        print('向量字典构造结束')

    def train(self):
        '''
        1.读文本中的训练样本
        2.划词
        3.添加wordlist
        4.重写vec词典

        :return:
        '''
        fp = open('extra/trainSample.txt', 'r')
        re = fp.readline()
        while re :
            train_sample = re.split(' ')
            q = train_sample[0]
            t = train_sample[1]
            t = t.replace('\n', '')
            self.add_words(q)
            while self.varification(q, t):
                i = 0
            re = fp.readline()
        fp.close()
        self.make_vec_file()
        print('训练结束')

    def add_words(self, q):
        words = Ut.file2List(TfConfig.words_path)
        fw = open(TfConfig.words_path, 'r+')
        fw.read()

        seg_list = jieba.cut(q)
        write_flag = True
        for s in seg_list:
            for w in words:
                if s == w:
                    write_flag = False
                    break
            if write_flag:
                fw.write(s +'\n')
            write_flag = True
        fw.close()


    def varification(self, q, t):
        print(q)
        threshold = self.cfg.threshold
        actual = self.simi_answermap(q)
        result = float(actual[0])
        section = actual[1]
        if t =='none':
            if result < threshold:
                return False
            elif result <0.6:
                self.cfg.set_threshold(result + 0.001)
                return True
            else:
                print(q)
                return False
        elif section == t and result >= threshold:
            if result - threshold < 0.01:
                self.cfg.set_threshold(result - 0.001)
            return False
        elif section == t and result < threshold:
            if threshold - result <0.01:
                self.cfg.set_threshold(result - 0.001)
            else:
                self.tuning(q, t)
            return False
        else:
            self.tuning(q, t)
            return False

    def tuning(self, q, t):
        self.cfgParser[t]['question'] = self.cfgParser[t]['question'] + q
        with open(self.cfg.answermap_path, 'w+') as fw:
            self.cfgParser.write(fw)
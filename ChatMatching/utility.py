class Utility:
    @staticmethod
    def file2List(file_name:str):
        r = []
        for ln in open(file_name):
            r.extend(ln.strip().split(' '))
        return r


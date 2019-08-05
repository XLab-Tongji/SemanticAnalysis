class Utility:
    @staticmethod
    def file2List(file_name:str):
        r = []
        for ln in open(file_name, encoding="UTF8"):
            r.extend(ln.strip().split(' '))
        return r


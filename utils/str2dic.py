class Str2Dic():
    def __init__(self, header, separator=","):
        if len(header) == 0:
            raise ValueError("Header empty")
        self.columns = header.split(separator)
        self.separator = separator

    def convert(self, row):
        values = row.split(self.separator)
        if len(values) == len(self.columns):
            if len(values) == len(self.columns):
                i = 0
                d = {}
                while i<len(values):
                    key = self.columns[i]
                    val = values[i]
                    d[key] = val
                    i=i+1
                return d
        else:
            raise ValueError("Row and Header lengths don't match.")
        
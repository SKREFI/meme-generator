class Log():
    end = '\033[0m'

    def __init__(self, str):
        self.fail(str)

    @classmethod
    def warning(cls, inp):
        print('\033[93m' + str(inp) + cls.end)

    @classmethod
    def fail(cls, inp):
        print('\033[91m' + str(inp) + cls.end)

    @classmethod
    def succes(cls, inp):
        print('\033[92m' + str(inp) + cls.end)

    @classmethod
    def debug(cls, inp):
        print('\033[94m' + str(inp) + cls.end)

    @classmethod
    def getAllStyles(cls):
        for i in range(100):
            print(f'\033[{i}mNumber{i}\033[0m')

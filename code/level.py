class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name

    def run(self):
        raise NotImplementedError("O nível precisa implementar run()")

class ALU:
    def __init__(self, ACC):
        self.ACC = ACC
        pass

    def add(self, data):
        #Results of ALUs are stored in ACC
        self.ACC.write(int(data[0]) + int(data[1]))
class Register:
    def __init__(self, initalValue):
        self.value = initalValue
    
    def read(self):
        return self.value
    
    def write(self, value):
        self.value = value

class MemoryCell(Register):
    def __init__(self, initalValue=None):
        super().__init__(initalValue)

class PC(Register):
    def __init__(self, initalValue=0):
        super().__init__(initalValue)

class MAR(Register):
    def __init__(self, initalValue=None):
        super().__init__(initalValue)

class MDR(Register):
    def __init__(self, initalValue=None):
        super().__init__(initalValue)

class CIR(Register):
    def __init__(self, initalValue=None):
        super().__init__(initalValue)

class ACC(Register):
    def __init__(self, initalValue=None):
        super().__init__(initalValue)
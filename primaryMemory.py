from registers import MemoryCell

class PrimaryMemory:
    def __init__(self, allocation=1000):
        #Stores a set of memory cells
        self.memory = [MemoryCell() for _ in range(allocation)]
    
    def addr(self, addr):
        #Retrieving the memory cell
        return self.memory[int(addr)]

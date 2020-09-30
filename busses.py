#This is not needed unless implicit mapping is needed
class AddressBus:
    def __init__(self):
        pass
    def addr(self, addr):
        return addr

#Data buses are used to interact with memory
class DataBus:
    def __init__(self, memory):
        self.memory = memory

    def write(self, addr, value):
        return self.memory.addr(addr).write(value)
    
    def read(self, addr):
        return self.memory.addr(addr).read()

#Unneeded until external interaction is called
class ControlBus:
    def __init__(self):
        pass
    #control bus acts as a return function for input
    def input(self):
        return input("")


    

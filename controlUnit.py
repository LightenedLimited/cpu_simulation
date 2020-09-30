from registers import PC, MAR, MDR, CIR, ACC
from alu import ALU

class ControlUnit:
    def __init__(self, dataBus, addressBus, controlBus):
        #Defining registers
        self.PC = PC()
        self.MAR = MAR()
        self.MDR = MDR()
        self.CIR = CIR()
        self.ACC = ACC()
        self.ALU = ALU(self.ACC)
        #Defining buses
        self.dataBus = dataBus
        self.addressBus = addressBus
        self.controlBus = controlBus
        self.opcode = {
            "add": self.add, 
            "store": self.storeACC, 
            "copy": self.copy,
            "input": self.input
        }
    def input(self, address):
        inputValue = self.controlBus.input()
        self.dataBus.write(self.addressBus.addr(address[0]), inputValue)

    def add(self, addresses):
        value_1 = self.dataBus.read(self.addressBus.addr(addresses[0]))
        value_2 =  self.dataBus.read(self.addressBus.addr(addresses[1]))
        self.ALU.add([value_1, value_2])

    def copy(self, addresses):
        addresses_1_value = self.dataBus.read(self.addressBus.addr(addresses[1]))
        self.dataBus.write(self.addressBus.addr(addresses[0]), addresses_1_value)

    #store acc into address
    def storeACC(self, addr):
        self.dataBus.write(self.addressBus.addr(addr), self.ACC.read())

    def decode(self):
        #Decode takes the raw data from the CIR, and splits it into the opcode and data of the data
        try:
            instruction = self.CIR.read()
            return instruction.split(" ")[0], instruction.split(" ")[1:]
        except:
            raise Exception("memory called is not an instruction")

    def execute(self):
        #ACC is only stored by the ALU
        opcode, data = self.decode()
        self.opcode[opcode](data)
        pass
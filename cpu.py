from controlUnit import ControlUnit
from busses import AddressBus, DataBus, ControlBus
from primaryMemory import PrimaryMemory

class CPU:
    def __init__(self):
        self.memory = PrimaryMemory()
        self.cu = ControlUnit(DataBus(self.memory), AddressBus(), ControlBus())
    
    def cycle(self):
        #fetch cycle
        #1. Copy PC value into MAR
        self.cu.MAR.write(self.cu.PC.read())
        #2. Increment PC value
        self.cu.PC.write(self.cu.PC.read() + 1)
        #3. Instruction found at MAR address copied into MDR
        instructionAddress = self.cu.MAR.read()
        instruction = self.cu.dataBus.read(self.cu.addressBus.addr(instructionAddress))
        self.cu.MDR.write(instruction)
        #4. Instruction copied from MDR to CIR
        self.cu.CIR.write(self.cu.MDR.read())
        #Execute
        #5. CU executes instruction
        self.cu.execute()
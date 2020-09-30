from cpu import CPU

cpu = CPU()

cpu.memory.addr(0).write("input 15")
cpu.memory.addr(1).write("input 16")
cpu.memory.addr(2).write("add 15 16")
cpu.cycle()
cpu.cycle()
cpu.cycle()
#three instructions, hence three cpu cycles
print(cpu.cu.ACC.read())
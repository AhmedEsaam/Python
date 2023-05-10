def SET_BIT(REG, BIT):
    Reg = int(REG)
    Bit = int(BIT)
    Reg |= (1<<Bit)
    return Reg

def CLR_BIT(REG, BIT):
    Reg = int(REG)
    Bit = int(BIT)
    Reg &= ~(1<<Bit)
    return Reg

def GET_BIT(REG, BIT):
    Reg = int(REG)
    Bit = int(BIT)
    return Reg & (1<<Bit)

def TOG_BIT(REG, BIT):
    Reg = int(REG)
    Bit = int(BIT)
    Reg ^= (1<<Bit)
    return Reg

print(bin(GET_BIT(16, 4)))
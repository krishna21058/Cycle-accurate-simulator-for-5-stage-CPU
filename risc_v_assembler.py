import sys

input = input()

instructions = []

inst=input.upper().split()
instructions.append(inst)
print(instructions)

register_dict = {
    "R0":"00000",
    "R1":"00001",
    "R2":"00010",
    "R3":"00011",
    "R4":"00100",
    "R5":"00101",
    "R6":"00110",
    "R7":"00111",
    "R8":"01000",
    "R9":"01001",
    "R10":"01010",
    "R11":"01011",
    "R12":"01100",
    "R13":"01101",
    "R14":"01110",
    "R15":"01111",
    "R16":"10000",
    "R17":"10001",
    "R18":"10010",
    "R19":"10011",
    "R20":"10100",
    "R21":"10101",
    "R22":"10110",
    "R23":"10111",
    "R24":"11000",
    "R25":"11001",
    "R26":"11010",
    "R27":"11011",
    "R28":"11100",
    "R29":"11101",
    "R30":"11110",
    "R31":"11111"
}



# type = [
#     {
#         "LUI": "0110111",
#         "AUIPC": "0010111",
#     }, {
#         "JAL": "1101111",
#         "rs": "11000",
#         "ls": "11001",
#         "movf": "00010"
#     }, {
#         "mov": "10011",
#         "div": "10111",
#         "not": "11101",
#         "cmp": "11110"
#     }, {
#         "ld": "10100",
#         "st": "10101"
#     }, {
#         "jmp": "11111",
#         "jlt": "01100",
#         "jgt": "01101",
#         "je": "01111"
#     }, {
#         "hlt": "01010"
#     }
# ]


type_dict={
    "LUI": "U",
    "AUIPC": "U",
    "JAL": "UJ",
    "JALR": "I",
    "BEQ": "SB",
    "BNE": "SB",
    "BLT": "SB",
    "BGE": "SB",
    "BLTU": "SB",
    "BGEU": "SB",
    "LB": "I",
    "LH": "I",
    "LW": "I",
    "LBU": "I",
    "LHU": "I",
    "SB": "S",
    "SH": "S",
    "SW": "S",
    "ADDI": "I",
    "SLTI": "I",
    "SLTIU": "I",
    "XORI": "I",
    "ORI": "I",
    "ANDI": "I",
    "SLLI": "R",
    "SRLI": "R",
    "SRAI": "R",
    "ADD": "R",
    "SUB": "R",
    "SLL": "R",
    "SLT": "R",
    "SLTU": "R",
    "XOR": "R",
    "SRL": "R",
    "SRA": "R",
    "OR": "R",
    "AND": "R",
}

funct3_dict={
    "BEQ":"000",
    "BNE":"001",
    "BLT":"100",
    "BGE":"101",
    "BLTU":"110",
    "BGEU":"111",
    "LB":"000",
    "LH":"001",
    "LW":"010",
    "LBU":"100",
    "LHU":"101",
    "SB":"000",
    "SW":"010",
    "SH":"001",
    "ADDI":"000",
    "SLTI":"010",
    "SLTIU":"011",
    "XORI":"100",
    "ORI":"110",
    "ANDI":"111",
    "SLLI":"001",
    "SRLI":"101",
    "SRAI":"101",
    "ADD":"000",
    "SUB":"000",
    "SLL":"001",
    "SLT":"010",
    "SLTU":"011",
    "XOR":"100",
    "SRL":"101",
    "SRA":"101",
    "OR":"110",
    "AND":"111" 
}

def main(instructions):
    for i in instructions:
        if(type_dict[i[0]]=="U"):
            print(U_type(i))
        elif(type_dict[i[0]]=="UJ"):
            print(UJ_type(i))
        elif(type_dict[i[0]]=="I"):
            print("I")
            print(I_type(i))
        elif(type_dict[i[0]]=="R"):
            print(R_type(i))
        elif(type_dict[i[0]]=="S"):
            print(S_type(i))
        elif(type_dict[i[0]]=="SB"):
            print(SB_type(i))
        

def U_type(i):
    assert len(i) == 3, "Wrong Instruction"
    assert i[0]=="LUI" or i[0]=="AUIPC", "Wrong Instruction"
    assert i[1] in register_dict, "Wrong Instruction"
    if (i[0]=="LUI"):
        opcode = "0110111"
    elif (i[0]=="AUIPC"):
        opcode = "0010111"
    rd = register_dict[i[1]]
    imm = bin(i[2]).replace("0b", "") 
    ans = imm+rd+opcode
    return ans


def UJ_type(i):
    assert len(i) == 3, "Wrong Instruction"
    assert i[0]=="JAL", "Wrong Instruction"
    assert i[1] in register_dict, "Wrong Instruction"
    inst=""
    for it in i:
        inst+=it
    opcode = "1101111"
    rd = register_dict[i[1]]
    val=int(i[3])
    imm = bin(val)[2:].zfill(12) 
    if(val<0):
        abs_value = abs(val)
        imm = bin(abs_value)[2:].zfill(12)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in imm)
        
        # Add 1 to the inverted binary to get the 2's complement representation.
        carry = 1
        result = []
        for bit in reversed(inverted_binary):
            if bit == '0':
                result.insert(0, str(carry))
                carry = 0
            else:
                result.insert(0, '1' if carry == 0 else '0')
        
        imm = ''.join(result)
    imm=imm[::-1]
    ans=imm[19]+imm[9::-1]+imm[10]+imm[18:11:-1]+" "+rd+" "+opcode
    ans = imm+rd+opcode 
    return ans


def S_type(i):
    opcode = "0100011"
    inst=""

    func3=funct3_dict[i[0]]+" "
    rs1 = register_dict[i[1]]+" "
    rs2 = register_dict[i[2]]+" "
    for it in i:
        inst+=it
    val=int(i[3])
    imm = bin(val)[2:].zfill(12) 
    if(val<0):
        abs_value = abs(val)
        imm = bin(abs_value)[2:].zfill(12)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in imm)
        
        # Add 1 to the inverted binary to get the 2's complement representation.
        carry = 1
        result = []
        for bit in reversed(inverted_binary):
            if bit == '0':
                result.insert(0, str(carry))
                carry = 0
            else:
                result.insert(0, '1' if carry == 0 else '0')
        
        imm = ''.join(result)
    
    ans=imm[0:7]+" "+rs2+rs1+func3+imm[7:12]+" "+opcode
    return ans


def I_type(i):
    opcode = (
        "1100111"
        if i[0] == "JALR"
        else "0000011"
        if i[0] in ["LB", "LH", "LW", "LBU", "LHU"]
        else "0010011"
    )
    rd = register_dict[i[1]]+" "
    rs1 = register_dict[i[2]]+" "
    func3=funct3_dict[i[0]]+" "
    val=int(i[3])
    imm = bin(val)[2:].zfill(12) 
    if(val<0):
        abs_value = abs(val)
        imm = bin(abs_value)[2:].zfill(12)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in imm)
        
        # Add 1 to the inverted binary to get the 2's complement representation.
        carry = 1
        result = []
        for bit in reversed(inverted_binary):
            if bit == '0':
                result.insert(0, str(carry))
                carry = 0
            else:
                result.insert(0, '1' if carry == 0 else '0')
        
        imm = ''.join(result)
    ans=imm + " " + rs1+func3+rd+opcode
    return ans

def SB_type(i):
    opcode = "1100011"
    rs1 = register_dict[i[1]]
    rs2 = register_dict[i[2]]
    funct3 = funct3_dict[i[0]]
    val=int(i[3])
    imm = bin(val)[2:].zfill(12) 
    if(val<0):
        abs_value = abs(val)
        imm = bin(abs_value)[2:].zfill(12)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in imm)
        
        # Add 1 to the inverted binary to get the 2's complement representation.
        carry = 1
        result = []
        for bit in reversed(inverted_binary):
            if bit == '0':
                result.insert(0, str(carry))
                carry = 0
            else:
                result.insert(0, '1' if carry == 0 else '0')
        
        imm = ''.join(result)

    imm=imm[::-1]
    ans=imm[11]+ " " + imm[9:3:-1] +" "+rs2+" "+rs1+" "+funct3+" "+imm[3::-1]+" "+imm[10]+" "+opcode
    return ans


def R_type(instruction):
    rd=register_dict[instruction[1]]+" "
    rs1=register_dict[instruction[2]]+" "
    funct3=funct3_dict[instruction[0]]+" "
    if instruction[0] in ["SLLI", "SRLI", "SRAI"]:
        opcode="0010011"
        shamt = format(int(instruction[3]), "05b")
        rs2=shamt
    else:
        opcode="0110011"
        rs2=register_dict[instruction[3]]
    if instruction[0] in ["SRAI","SUB","SRA"]:
        imm_at_end="0100000"
    else:
        imm_at_end="0000000"
    
    return(imm_at_end+" "+rs2+" "+ rs1+funct3+rd+" "+opcode)

main(instructions)
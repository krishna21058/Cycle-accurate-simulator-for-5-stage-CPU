#simulator

#opcode to function
opcode_to_func = {
    '0000': 'add',
    '0001': 'sub',
    '0010': 'mul',
    '0011': 'div',
    '0100': 'mov',
    '0101': 'ld',
    '0110': 'st',
    '0111': 'b',
    '1000': 'beq',
    '1001': 'bgt',
    '1010': 'ldi',
    '1011': 'sti',
    '1100': 'hlt'
}


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
#reverse this dictionary
register_dict_rev = {v: k for k, v in register_dict.items()}
# print(register_dict_rev)

#initialise all register values to 0
reg_val={
    "R0":0,
    "R1":0,
    "R2":0,
    "R3":0,
    "R4":0,
    "R5":0,
    "R6":0,
    "R7":0,
    "R8":0,
    "R9":0,
    "R10":0,
    "R11":0,
    "R12":0,
    "R13":0,
    "R14":0,
    "R15":0,
    "R16":0,
    "R17":0,
    "R18":0,
    "R19":0,
    "R20":0,
    "R21":0,
    "R22":0,
    "R23":0,
    "R24":0,
    "R25":0,
    "R26":0,
    "R27":0,
    "R28":0,
    "R29":0,
    "R30":0,
    "R31":0
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
#reverse this
funct3_dict_rev = {v: k for k, v in funct3_dict.items()}


# funct7_dict={
#     "SUB":"0100000",
#     "SRA":"0100000",
#     "SRL":"0000000",
#     "MUL":"0000001",
#     "DIV":"0000001",
#     "SLL":"0000000",
#     "ADD":"0000000",
#     "XOR":"0000000",
#     "OR":"0000000",
#     "AND":"0000000"
# }

#opcode to function type
opcode_to_instr = {
    '0110111': 'LUI',
    '0010111': 'AUIPC',
    '1101111': 'JAL',
    '1100111': 'JALR',
    '1100011': {
        '000': 'BEQ',
        '001': 'BNE',
        '100': 'BLT',
        '101': 'BGE',
        '110': 'BLTU',
        '111': 'BGEU',
    },
    '0000011': {
        '000': 'LB',
        '001': 'LH',
        '010': 'LW',
        '100': 'LBU',
        '101': 'LHU',
    },
    '0100011': {
        '000': 'SB',
        '001': 'SH',
        '010': 'SW',
    },
    '0010011': {
        '000': 'ADDI',
        '010': 'SLTI',
        '011': 'SLTIU',
        '100': 'XORI',
        '110': 'ORI',
        '111': 'ANDI',
    },
    '0010011': {
        '001': 'SLLI',
        '101': 'SRLI',
        '101': 'SRAI',
    },
    '0110011': {
        '000': 'ADD',
        '000': 'SUB',
        '001': 'SLL',
        '010': 'SLT',
        '011': 'SLTU',
        '100': 'XOR',
        '101': 'SRL',
        '101': 'SRA',
        '110': 'OR',
        '111': 'AND',
    }
}



fopen=open("binary.txt","r")

# Read the file
data=fopen.read()
bin_instr=data.split("\n")
print(bin_instr)

for i in bin_instr:
    opcode=i[25:32]
    print(opcode)
    if opcode_to_instr[opcode].__class__ == str:
        func=opcode_to_instr[opcode]
        if func=="LUI":
            lui(i)
        elif func=="AUIPC":
            auipc(i)
        elif func=="JAL":
            jal(i)
        elif func=="JALR":
            jalr(i)

        
    else:
        func=opcode_to_instr[opcode][i[17:20]]
        if func=="BEQ":
            beq(i)
        elif func=="BNE":
            bne(i)
        elif func=="BLT":
            blt(i)
        elif func=="BGE":
            bge(i)
        elif func=="BLTU":
            bltu(i)
        elif func=="BGEU":
            bgeu(i)
        elif func=="LB":
            lb(i)
        elif func=="LH":
            lh(i)
        elif func=="LW":
            lw(i)
        elif func=="LBU":
            lbu(i)
        elif func=="LHU":
            lhu(i)
        elif func=="SB":
            sb(i)
        elif func=="SH":
            sh(i)
        elif func=="SW":
            sw(i)
        elif func=="ADDI":
            addi(i)
        elif func=="SLTI":
            slti(i)
        elif func=="SLTIU":
            sltiu(i)
        elif func=="XORI":
            xori(i)
        elif func=="ORI":
            ori(i)
        elif func=="ANDI":
            andi(i)
        elif func=="SLLI":
            slli(i)
        elif func=="SRLI":
            srli(i)
        elif func=="SRAI":
            srai(i)
        elif func=="ADD":
            add(i)
        elif func=="SUB":
            sub(i)
        elif func=="SLL":
            sll(i)
        elif func=="SLT":
            slt(i)
        elif func=="SLTU":
            sltu(i)
        elif func=="XOR":
            xor(i)
        elif func=="SRL":
            srl(i)
        elif func=="SRA":
            sra(i)
        elif func=="OR":
            func_or(i)
        elif func=="AND":
            func_and(i)

#create functions for all instructions
def lui(i):
    rd=register_dict_rev[i[20:25]]
    imm=i[0:20]
    imm=int(imm,2)
    reg_val[rd]=imm
    print("LUI")
    print(reg_val)

def auipc(i):
    rd=register_dict_rev[i[20:25]]
    imm=i[0:20]
    imm=int(imm,2)
    reg_val[rd]=reg_val["R0"]+imm
    print("AUIPC")
    print(reg_val)

def jal(i):
    rd=register_dict_rev[i[20:25]]
    imm=i[0]+i[12:20]+i[11]+i[1:11]
    imm=int(imm,2)
    reg_val[rd]=reg_val["R0"]+4
    reg_val["R0"]=reg_val["R0"]+imm
    print("JAL")
    print(reg_val)

def jalr(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val["R0"]+4
    reg_val["R0"]=reg_val[rs1]+imm
    print("JALR")
    print(reg_val)

def beq(i):
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    imm=i[0]+i[24]+i[1:7]+i[20:24]+"0"
    imm=int(imm,2)
    if reg_val[rs1]==reg_val[rs2]:
        reg_val["R0"]=reg_val["R0"]+imm
    print("BEQ")
    print(reg_val)

def bne(i):
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    imm=i[0]+i[24]+i[1:7]+i[20:24]+"0"
    imm=int(imm,2)
    if reg_val[rs1]!=reg_val[rs2]:
        reg_val["R0"]=reg_val["R0"]+imm
    print("BNE")
    print(reg_val)

def blt(i):
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    imm=i[0]+i[24]+i[1:7]+i[20:24]+"0"
    imm=int(imm,2)
    if reg_val[rs1]<reg_val[rs2]:
        reg_val["R0"]=reg_val["R0"]+imm
    print("BLT")
    print(reg_val)

def bge(i):
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    imm=i[0]+i[24]+i[1:7]+i[20:24]+"0"
    imm=int(imm,2)
    if reg_val[rs1]>=reg_val[rs2]:
        reg_val["R0"]=reg_val["R0"]+imm
    print("BGE")
    print(reg_val)

def bltu(i):
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    imm=i[0]+i[24]+i[1:7]+i[20:24]+"0"
    imm=int(imm,2)
    if reg_val[rs1]<reg_val[rs2]:
        reg_val["R0"]=reg_val["R0"]+imm
    print("BLTU")
    print(reg_val)

def bgeu(i):
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    imm=i[0]+i[24]+i[1:7]+i[20:24]+"0"
    imm=int(imm,2)
    if reg_val[rs1]>=reg_val[rs2]:
        reg_val["R0"]=reg_val["R0"]+imm
    print("BGEU")
    print(reg_val)

def lb(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val[rs1]+imm
    print("LB")
    print(reg_val)

def lh(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val[rs1]+imm
    print("LH")
    print(reg_val)

def lw(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val[rs1]+imm
    print("LW")
    print(reg_val)

def lbu(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val[rs1]+imm
    print("LBU")
    print(reg_val)

def lhu(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val[rs1]+imm
    print("LHU")
    print(reg_val)

def sb(i):
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    imm=i[0:7]+i[20:25]
    imm=int(imm,2)
    reg_val[rs1]=reg_val[rs2]+imm
    print("SB")
    print(reg_val)

def sh(i):
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    imm=i[0:7]+i[20:25]
    imm=int(imm,2)
    reg_val[rs1]=reg_val[rs2]+imm
    print("SH")
    print(reg_val)

def sw(i):
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    imm=i[0:7]+i[20:25]
    imm=int(imm,2)
    reg_val[rs1]=reg_val[rs2]+imm
    print("SW")
    print(reg_val)

def addi(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val[rs1]+imm
    print("ADDI")
    print(reg_val)

def slti(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    if reg_val[rs1]<imm:
        reg_val[rd]=1
    else:
        reg_val[rd]=0
    print("SLTI")
    print(reg_val)

def sltiu(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    if reg_val[rs1]<imm:
        reg_val[rd]=1
    else:
        reg_val[rd]=0
    print("SLTIU")
    print(reg_val)

def xori(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val[rs1]^imm
    print("XORI")
    print(reg_val)

def ori(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val[rs1]|imm
    print("ORI")
    print(reg_val)

def andi(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    imm=i[0:12]
    imm=int(imm,2)
    reg_val[rd]=reg_val[rs1]&imm
    print("ANDI")
    print(reg_val)

def slli(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    shamt=i[7:12]
    shamt=int(shamt,2)
    reg_val[rd]=reg_val[rs1]<<shamt
    print("SLLI")
    print(reg_val)

def srli(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    shamt=i[7:12]
    shamt=int(shamt,2)
    reg_val[rd]=reg_val[rs1]>>shamt
    print("SRLI")
    print(reg_val)

def srai(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    shamt=i[7:12]
    shamt=int(shamt,2)
    reg_val[rd]=reg_val[rs1]>>shamt
    print("SRAI")
    print(reg_val)

def add(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    reg_val[rd]=reg_val[rs1]+reg_val[rs2]
    print("ADD")
    print(reg_val)

def sub(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    reg_val[rd]=reg_val[rs1]-reg_val[rs2]
    print("SUB")
    print(reg_val)

def sll(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    reg_val[rd]=reg_val[rs1]<<reg_val[rs2]
    print("SLL")
    print(reg_val)

def slt(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    if reg_val[rs1]<reg_val[rs2]:
        reg_val[rd]=1
    else:
        reg_val[rd]=0
    print("SLT")
    print(reg_val)

def sltu(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    if reg_val[rs1]<reg_val[rs2]:
        reg_val[rd]=1
    else:
        reg_val[rd]=0
    print("SLTU")
    print(reg_val)

def xor(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    reg_val[rd]=reg_val[rs1]^reg_val[rs2]
    print("XOR")
    print(reg_val)

def srl(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    reg_val[rd]=reg_val[rs1]>>reg_val[rs2]
    print("SRL")
    print(reg_val)

def sra(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    reg_val[rd]=reg_val[rs1]>>reg_val[rs2]
    print("SRA")
    print(reg_val)

def func_or(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    reg_val[rd]=reg_val[rs1]|reg_val[rs2]
    print("OR")
    print(reg_val)

def func_and(i):
    rd=register_dict_rev[i[20:25]]
    rs1=register_dict_rev[i[12:17]]
    rs2=register_dict_rev[i[7:12]]
    reg_val[rd]=reg_val[rs1]&reg_val[rs2]
    print("AND")
    print(reg_val)

# main(bin_instr)
# print(reg_val)

# simulator
import pdb
import random

# opcode to function
opcode_to_func = {
    "0000": "add",
    "0001": "sub",
    "0010": "mul",
    "0011": "div",
    "0100": "mov",
    "0101": "ld",
    "0110": "st",
    "0111": "b",
    "1000": "beq",
    "1001": "bgt",
    "1010": "ldi",
    "1011": "sti",
    "1100": "hlt",
}


register_dict = {
    "R0": "00000",
    "R1": "00001",
    "R2": "00010",
    "R3": "00011",
    "R4": "00100",
    "R5": "00101",
    "R6": "00110",
    "R7": "00111",
    "R8": "01000",
    "R9": "01001",
    "R10": "01010",
    "R11": "01011",
    "R12": "01100",
    "R13": "01101",
    "R14": "01110",
    "R15": "01111",
    "R16": "10000",
    "R17": "10001",
    "R18": "10010",
    "R19": "10011",
    "R20": "10100",
    "R21": "10101",
    "R22": "10110",
    "R23": "10111",
    "R24": "11000",
    "R25": "11001",
    "R26": "11010",
    "R27": "11011",
    "R28": "11100",
    "R29": "11101",
    "R30": "11110",
    "R31": "11111",
}
# reverse this dictionary
register_dict_rev = {v: k for k, v in register_dict.items()}
# print(register_dict_rev)

# initialise all register values to 0
reg_val = {
    "R0": 1,
    "R1": 1,
    "R2": 1,
    "R3": 1,
    "R4": 1,
    "R5": 1,
    "R6": 1,
    "R7": 1,
    "R8": 1,
    "R9": 1,
    "R10": 1,
    "R11": 1,
    "R12": 1,
    "R13": 1,
    "R14": 1,
    "R15": 1,
    "R16": 1,
    "R17": 1,
    "R18": 1,
    "R19": 1,
    "R20": 1,
    "R21": 1,
    "R22": 1,
    "R23": 1,
    "R24": 1,
    "R25": 1,
    "R26": 1,
    "R27": 1,
    "R28": 1,
    "R29": 1,
    "R30": 1,
    "R31": 1,
}

funct3_dict = {
    "BEQ": "000",
    "BNE": "001",
    "BLT": "100",
    "BGE": "101",
    "BLTU": "110",
    "BGEU": "111",
    "LB": "000",
    "LH": "001",
    "LW": "010",
    "LBU": "100",
    "LHU": "101",
    "SB": "000",
    "SW": "010",
    "SH": "001",
    "ADDI": "000",
    "SLTI": "010",
    "SLTIU": "011",
    "XORI": "100",
    "ORI": "110",
    "ANDI": "111",
    "SLLI": "001",
    "SRLI": "101",
    "SRAI": "101",
    "ADD": "000",
    "SUB": "000",
    "SLL": "001",
    "SLT": "010",
    "SLTU": "011",
    "XOR": "100",
    "SRL": "101",
    "SRA": "101",
    "OR": "110",
    "AND": "111",
}
# reverse this
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

# opcode to function type
opcode_to_instr = {
    "0110111": "LUI",
    "0010111": "AUIPC",
    "1101111": "JAL",
    "1100111": "JALR",
    "1100011": {
        "000": "BEQ",
        "001": "BNE",
        "100": "BLT",
        "101": "BGE",
        "110": "BLTU",
        "111": "BGEU",
    },
    "0000011": {
        "000": "LB",
        "001": "LH",
        "010": "LW",
        "100": "LBU",
        "101": "LHU",
    },
    "0100011": {
        "000": "SB",
        "001": "SH",
        "010": "SW",
    },
    "0010011": {
        "000": "ADDI",
        "010": "SLTI",
        "011": "SLTIU",
        "100": "XORI",
        "110": "ORI",
        "111": "ANDI",
    },
    "0010011": {
        "001": "SLLI",
        "101": "SRLI",
        "101": "SRAI",
    },
    "0110011": {
        "000": "ADD",
        "000": "SUB",
        "001": "SLL",
        "010": "SLT",
        "011": "SLTU",
        "100": "XOR",
        "101": "SRL",
        "101": "SRA",
        "110": "OR",
        "111": "AND",
    },
}


class Instruction_Memory:
    def __init__(self):
        # self.access_time = access_time
        self.memory = list()

    def initialize(self):
        f = open("binary.txt", "r")
        data = f.read()
        bin_instr = data.split("\n")
        self.memory = bin_instr
        return len(self.memory)

    def getData(self, row):
        return self.memory[row // 4]


PC = 0

mem_reg = {"4000": 0, "4004": 0, "4008": 0, "400c": 0, "4010": 0}

# def fetch(PC, IM):
#     PC = PC + 4
#     return IM.getData(PC)

# def decode(instruction):
#     opcode = instruction[25:32]
#     if opcode == "00


class Fetch:
    def __init__(self, imem):
        # self.dmem=dmem
        self.binary = 0
        self.imem = imem

    def fetch(self, PC):
        self.binary = self.imem.getData(PC)

    def sendToDecode(self):
        return self.binary


class Decode:
    def _init_(self, imem, reg_val):
        self.register_dict = reg_val
        self.immediate = 0
        self.fetch = Fetch(self.imem)
        self.binary = self.fetch.sendToDecode()
        self.imem = imem
        self.rd = ""
        self.rs1 = ""
        self.rs2 = ""

    def decode(self, PC):
        if self.binary == 0:
            return
        elif self.binary[25:32] == "0110111":
            # LUI
            self.rd = register_dict_rev[self.binary[20:25]]
            self.immediate = int(self.binary[0:20], 2)
        elif self.binary[25:32] == "0010111":
            self.rd = register_dict_rev[self.binary[20:25]]
            self.immediate = int(self.binary[0:20], 2)
        elif self.binary[25:32] == "1101111":
            self.rd = register_dict_rev[self.binary[20:25]]
            self.immediate = int(
                self.binary[0]
                + self.binary[12:20]
                + self.binary[11]
                + self.binary[1:11],
                2,
            )
        elif self.binary[25:32] == "1100111":
            self.rs1 = register_dict_rev[self.binary[12:17]]
            self.rd = register_dict_rev[self.binary[20:25]]
            self.immediate = int(self.binary[0:12], 2)
        elif self.binary[25:32] == "1100011":
            self.rs1 = register_dict_rev[self.binary[12:17]]
            self.rs2 = register_dict_rev[self.binary[7:12]]
            self.immediate = int(
                self.binary[0]
                + self.binary[24]
                + self.binary[1:7]
                + self.binary[20:24],
                2,
            )
        elif self.binary[25:32] == "0000011":
            self.rs1 = register_dict_rev[self.binary[12:17]]
            self.rd = register_dict_rev[self.binary[20:25]]
            self.immediate = int(self.binary[0:12], 2)
        elif self.binary[25:32] == "0100011":
            self.rs1 = register_dict_rev[self.binary[12:17]]
            self.rs2 = register_dict_rev[self.binary[7:12]]
            self.immediate = int(self.binary[0:7] + self.binary[20:25], 2)
        elif self.binary[25:32] == "0010011":
            self.rs1 = register_dict_rev[self.binary[12:17]]
            self.rd = register_dict_rev[self.binary[20:25]]
            self.immediate = int(self.binary[0:12], 2)
        elif self.binary[25:32] == "0110011":
            self.rs1 = register_dict_rev[self.binary[12:17]]
            self.rs2 = register_dict_rev[self.binary[7:12]]
            self.rd = register_dict_rev[self.binary[20:25]]
            self.immediate = 0
        # Assumption : kar lena yaad se

    def send_to_execute(self):
        return [self.rd, self.rs1, self.rs2, self.immediate, self.binary]


class Execute:
    def __init__(self, opcode_to_instr):
        self.decode_result = Decode.send_to_execute()
        # self.reg1_val=0
        # self.reg2_val=0
        self.reg_buffer = ""
        self.buf_val = 0
        self.binary = self.decode_result[-1]
        self.opcode_to_instr = opcode_to_instr

    def execute(self, PC):
        opcode = self.binary[25:32]
        if self.opcode_to_instr[opcode].__class__ == str:
            func = opcode_to_instr[opcode]
            if func == "LUI":
                self.reg_buffer = self.decode_result[0]
                self.buf_val = self.decode_result[3]
            elif func == "AUIPC":
                # auipc(i)
                self.reg_buffer = self.decode_result[0]
                self.buf_val = self.decode_result[3] + PC
                # reg_val[self.decode_result[0]] = reg_val["R0"] + self.decode_result[3]
        else:
            func = self.opcode_to_instr[opcode][self.binary[17:20]]
            if func == "BEQ":
                # beq(i)
                if reg_val[self.decode_result[1]] == reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] - 4
            elif func == "BNE":
                # bne(i)
                if reg_val[self.decode_result[1]] != reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] - 4
            elif func == "BLT":
                # blt(i)
                if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] - 4
            elif func == "BGE":
                # bge(i)
                if reg_val[self.decode_result[1]] >= reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] - 4
            elif func == "BLTU":
                # bltu(i)
                if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] - 4
            elif func == "BGEU":
                # bgeu(i)
                if reg_val[self.decode_result[1]] >= reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] - 4
            elif func == "LB":
                # lb(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] + self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "LH":
                # lh(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] + self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "LW":
                # lw(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] + self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "LBU":
                # lbu(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] + self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "LHU":
                # lhu(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] + self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "SB":
                # sb(i)
                # reg_val[self.decode_result[1]] = (
                #     reg_val[self.decode_result[2]] + self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[1]
                self.buf_val = reg_val[self.decode_result[2]] + self.decode_result[3]
            elif func == "SH":
                # sh(i)
                # reg_val[self.decode_result[1]] = (
                #     reg_val[self.decode_result[2]] + self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[1]
                self.buf_val = reg_val[self.decode_result[2]] + self.decode_result[3]
            elif func == "SW":
                # sw(i)
                # reg_val[self.decode_result[1]] = (
                #     reg_val[self.decode_result[2]] + self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[1]
                self.buf_val = reg_val[self.decode_result[2]] + self.decode_result[3]
            elif func == "ADDI":
                # addi(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] + self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "SLTI":
                # slti(i)
                # if reg_val[self.decode_result[1]] < self.decode_result[3]:
                #     reg_val[self.decode_result[0]] = 1
                # else:
                #     reg_val[self.decode_result[0]] = 0
                self.reg_buffer = self.decode_result[0]
                if reg_val[self.decode_result[1]] < self.decode_result[3]:
                    self.buf_val = 1
                else:
                    self.buf_val = 0

            elif func == "SLTIU":
                # sltiu(i)
                # if reg_val[self.decode_result[1]] < self.decode_result[3]:
                #     reg_val[self.decode_result[0]] = 1
                # else:
                #     reg_val[self.decode_result[0]] = 0
                self.reg_buffer = self.decode_result[0]
                if reg_val[self.decode_result[1]] < self.decode_result[3]:
                    self.buf_val = 1
                else:
                    self.buf_val = 0
            elif func == "XORI":
                # xori(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] ^ self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] ^ self.decode_result[3]
            elif func == "ORI":
                # ori(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] | self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] | self.decode_result[3]
            elif func == "ANDI":
                # andi(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] & self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] & self.decode_result[3]
            elif func == "SLLI":
                # slli(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] << self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] << self.decode_result[3]
            elif func == "SRLI":
                # srli(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] >> self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] >> self.decode_result[3]
            elif func == "SRAI":
                # srai(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] >> self.decode_result[3]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] >> self.decode_result[3]
            elif func == "ADD":
                # add(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] + reg_val[self.decode_result[2]]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] + reg_val[self.decode_result[2]]
                )
            elif func == "SUB":
                # sub(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] - reg_val[self.decode_result[2]]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] - reg_val[self.decode_result[2]]
                )
            elif func == "SLL":
                # sll(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] << reg_val[self.decode_result[2]]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] << reg_val[self.decode_result[2]]
                )
            elif func == "SLT":
                # slt(i)
                # if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                #     reg_val[self.decode_result[0]] = 1
                # else:
                #     reg_val[self.decode_result[0]] = 0
                self.reg_buffer = self.decode_result[0]
                if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                    self.buf_val = 1
                else:
                    self.buf_val = 0
            elif func == "SLTU":
                # sltu(i)
                # if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                #     reg_val[self.decode_result[0]] = 1
                # else:
                #     reg_val[self.decode_result[0]] = 0
                self.reg_buffer = self.decode_result[0]
                if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                    self.buf_val = 1
                else:
                    self.buf_val = 0
            elif func == "XOR":
                # xor(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] ^ reg_val[self.decode_result[2]]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] ^ reg_val[self.decode_result[2]]
                )
            elif func == "SRL":
                # srl(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] >> reg_val[self.decode_result[2]]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] >> reg_val[self.decode_result[2]]
                )
            elif func == "SRA":
                # sra(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] >> reg_val[self.decode_result[2]]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] >> reg_val[self.decode_result[2]]
                )
            elif func == "OR":
                # func_or(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] | reg_val[self.decode_result[2]]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] | reg_val[self.decode_result[2]]
                )
            elif func == "AND":
                # func_and(i)
                # reg_val[self.decode_result[0]] = (
                #     reg_val[self.decode_result[1]] & reg_val[self.decode_result[2]]
                # )
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] & reg_val[self.decode_result[2]]
                )
        PC = PC + 4

        return PC

    def send_to_memory(self):
        return [
            self.rd,
            self.rs1,
            self.rs2,
            self.immediate,
            self.binary,
            self.reg_buffer,
            self.buf_val,
        ]

class Memory:
    def __init__(self,mem):
        self.execute_result = Execute.send_to_memory()
        self.binary = self.execute_result[4]
        self.loadval = 0
        self.loadreg = ""
        self.mem1024=mem

    def execute(self):
        opcode = self.binary[25:32]
        if opcode == "0100011":
            # store
            mem_addr=self.execute_result[6]
            data_to_store = reg_val[self.execute_result[5]]
            self.mem1024[mem_addr] = data_to_store
        # check whether writeback or memory stage
        elif opcode == "0000011":
            # load
            mem_addr= self.execute_result[6]
            reg_val[self.execute_result[5]]=self.mem1024[mem_addr]

    def send_to_writeback(self):
        return [
            self.loadval,
            self.loadreg,
            self.binary,
            self.execute_result[5],
            self.execute_result[6],
        ]


class Writeback:
    def __init__(self):
        self.memory_result = Memory.send_to_writeback()
        self.binary = self.memory_result[2]
        self.loadval = self.memory_result[0]
        self.loadreg = self.memory_result[1]
        self.reg_buffer = self.memory_result[3]
        self.buf_val = self.memory_result[4]

    def writeback(self):
        opcode = self.binary[25:32]
        if opcode == "0000011":
            # load
            reg_val[self.loadreg] = self.loadval
        else:
            reg_val[self.reg_buffer] = self.buf_val


def check_data_hazard(prev_instr,cur_instr):
    if prev_instr[0]==cur_instr[1] or prev_instr[0]==cur_instr[2]:
        return True
    else:
        return False
    

def __main__():
    IM = Instruction_Memory()
    no_instr = IM.initialize()
    PC = 0
    memory1024 = [random.randint(0, 255) for _ in range(1024)]
    end=0
    # pipeline_arr =  [-1,-1,-1,-1,-1]
    # # F D X M W

    # end=0
    # i=0
    # while end!=1:
    #     cur_ins=IM.memory[i]
    #     if(i>0):
    #         prev_ins=IM.memory[i-1]
    #         # if(check_data_hazard(prev_ins,cur_ins)):
    #     if pipeline_arr[0]==-1:
    #         fetchvar = Fetch(IM)
    #         fetchvar.fetch(PC)
    #         pipeline_arr[0]=i
    #     elif pipeline_arr[1]==-1:
    #         decodevar = Decode(IM, reg_val)
    #         decodevar.decode(PC)
    #         pipeline_arr[0]=-1
    #         pipeline_arr[1]=i
    #         if pipeline_arr[0]==-1:
    #             fetchvar = Fetch(IM)
    #             fetchvar.fetch(PC)
    #             pipeline_arr[0]=i

    #     elif pipeline_arr[2]==-1:
    #         executevar=Execute(opcode_to_instr)
    #         executevar.execute(PC)
    #         pipeline_arr[1]=-1
    #         pipeline_arr[2]=i
    #         if pipeline_arr[1]==-1:
    #             decodevar = Decode(IM, reg_val)
    #             decodevar.decode(PC)
    #             pipeline_arr[1]=i

    # pipeline_arr=[0,-1,-1,-1,-1]
    # i=0
    # while i<no_instr and end==0:
    # #   cur_ins=IM.memory[i]
    #   if(pipeline_arr[0]==i):
    #     # fetch
    #     fetchvar = Fetch(IM)
    #     fetchvar.fetch(PC)
    #     pipeline_arr[1]=pipeline_arr[0]
    #     pipeline_arr[0]+=1

    #   elif pipeline_arr[1]==i:
    #     # decode
    #     decodevar = Decode(IM, reg_val)
    #     decodevar.decode(PC)

    #   elif pipeline_arr[2]==i:
    #     # p

    pipeline_arr = [0, 0, 0, 0, 0]
    no_instr=5
    end=0
    i = 0
    stage = {}
    for i in range(no_instr):
        stage[i] = "F"
    cycle=0
    
    while end == 0:
        # for i in range(no_instr):
          
        # print("\n")
        print("Cycle",cycle)
        cycle+=1
        for i in range(0,len(stage)):
            print(i, stage[i])
        for i in range(no_instr):
            # instruc = inst_mem.getData(i)
            if stage[i] == "F" and pipeline_arr[0] == 0:
                pipeline_arr[0] = 1
                stage[i] = "D"

            elif stage[i] == "D" and pipeline_arr[1] == 0:
                # decode
                pipeline_arr[1] = 1
                stage[i] = "X"

            elif stage[i] == "X" and pipeline_arr[2] == 0:
                # execute
                pipeline_arr[2] = 1
                stage[i] = "M"

            elif stage[i] == "M" and pipeline_arr[3] == 0:
                # memory
                pipeline_arr[3] = 1

                stage[i] = "W"

            elif stage[i] == "W" and pipeline_arr[4] == 0:
                # writeback

                pipeline_arr[4] = 1
                stage[i] = ""
          
        
            if stage[no_instr - 1] == "W":
                end = 1
        pipeline_arr=[0,0,0,0,0]
        print("\n")
    print("Cycle",cycle)
    for i in range(0,len(stage)):
      print(i, stage[i])


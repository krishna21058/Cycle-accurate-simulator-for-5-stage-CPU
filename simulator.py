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
    def __init__(self,pc_update=1):
        
        self.memory = list()

    def initialize(self):
        f = open("test.txt", "r")
        data = f.read()
        bin_instr = data.split("\n")
        self.memory = bin_instr
        
    def list_of_instr(self):
        f = open("test.txt", "r")
        data = f.read()
        bin_instr = data.split("\n")
        return bin_instr
    def getData(self, row):
        return self.memory[row]
    def get_len(sef):
        f = open("test.txt", "r")
        data = f.read()
        bin_instr = data.split("\n")
        return len(bin_instr)

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
    def __init__(self, imem, reg_val):
        self.register_dict = reg_val
        self.immediate = 0
        self.imem = imem
        self.fetch = Fetch(self.imem)
        self.binary = self.fetch.sendToDecode()
        self.rd = ""
        self.rs1 = ""
        self.rs2 = ""

    def decode(self):
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
    def __init__(self, opcode_to_instr,imem):
        self.imem = imem
        self.decode = Decode(self.imem,reg_val)
        self.decode_result = self.decode.send_to_execute()

        self.reg_buffer = ""
        self.buf_val = 0
        self.binary = self.decode_result[-1]
        self.opcode_to_instr = opcode_to_instr

    def execute(self, PC):
        print("**************",self.binary)
        opcode = self.binary[25:32]
        if self.opcode_to_instr[opcode].__class__ == str:
            func = opcode_to_instr[opcode]
            if func == "LUI":
                self.reg_buffer = self.decode_result[0]
                self.buf_val = self.decode_result[3]
            elif func == "AUIPC":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = self.decode_result[3] + PC
                # reg_val[self.decode_result[0]] = reg_val["R0"] + self.decode_result[3]
        else:
            func = self.opcode_to_instr[opcode][self.binary[17:20]]
            if func == "BEQ":

                if reg_val[self.decode_result[1]] == reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] 
            elif func == "BNE":
   
                if reg_val[self.decode_result[1]] != reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] 
            elif func == "BLT":
   
                if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] 
            elif func == "BGE":

                if reg_val[self.decode_result[1]] >= reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] 
            elif func == "BLTU":

                if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] 
            elif func == "BGEU":

                if reg_val[self.decode_result[1]] >= reg_val[self.decode_result[2]]:
                    PC += self.decode_result[3] 
            elif func == "LB":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "LH":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "LW":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "LBU":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "LHU":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "SB":

                self.reg_buffer = self.decode_result[1]
                self.buf_val = reg_val[self.decode_result[2]] + self.decode_result[3]
            elif func == "SH":

                self.reg_buffer = self.decode_result[1]
                self.buf_val = reg_val[self.decode_result[2]] + self.decode_result[3]
            elif func == "SW":

                self.reg_buffer = self.decode_result[1]
                self.buf_val = reg_val[self.decode_result[2]] + self.decode_result[3]
            elif func == "ADDI":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] + self.decode_result[3]
            elif func == "SLTI":

                self.reg_buffer = self.decode_result[0]
                if reg_val[self.decode_result[1]] < self.decode_result[3]:
                    self.buf_val = 1
                else:
                    self.buf_val = 0

            elif func == "SLTIU":

                self.reg_buffer = self.decode_result[0]
                if reg_val[self.decode_result[1]] < self.decode_result[3]:
                    self.buf_val = 1
                else:
                    self.buf_val = 0
            elif func == "XORI":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] ^ self.decode_result[3]
            elif func == "ORI":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] | self.decode_result[3]
            elif func == "ANDI":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] & self.decode_result[3]
            elif func == "SLLI":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] << self.decode_result[3]
            elif func == "SRLI":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] >> self.decode_result[3]
            elif func == "SRAI":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = reg_val[self.decode_result[1]] >> self.decode_result[3]
            elif func == "ADD":
                
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] + reg_val[self.decode_result[2]]
                )
            elif func == "SUB":
     
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] - reg_val[self.decode_result[2]]
                )
            elif func == "SLL":
 
                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] << reg_val[self.decode_result[2]]
                )
            elif func == "SLT":

                self.reg_buffer = self.decode_result[0]
                if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                    self.buf_val = 1
                else:
                    self.buf_val = 0
            elif func == "SLTU":

                self.reg_buffer = self.decode_result[0]
                if reg_val[self.decode_result[1]] < reg_val[self.decode_result[2]]:
                    self.buf_val = 1
                else:
                    self.buf_val = 0
            elif func == "XOR":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] ^ reg_val[self.decode_result[2]]
                )
            elif func == "SRL":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] >> reg_val[self.decode_result[2]]
                )
            elif func == "SRA":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] >> reg_val[self.decode_result[2]]
                )
            elif func == "OR":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] | reg_val[self.decode_result[2]]
                )
            elif func == "AND":

                self.reg_buffer = self.decode_result[0]
                self.buf_val = (
                    reg_val[self.decode_result[1]] & reg_val[self.decode_result[2]]
                )
        # PC = PC + 4

        # return PC

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







class Instruction:

    def __init__(self,Binary) :
        self.binary=Binary
        self.F_starting=-1
        self.F_ending=-1
        self.D_starting=-1
        self.D_ending=-1
        self.Ex=-1
        self.Mem=-1
        self.Wr=-1
    def check_hazard(prev_instrction,self):
        
        prev_rd=register_dict_rev[prev_instrction.binary[20:25]]
        rs1_current=register_dict_rev[self.binary[12:17]]
        print(prev_rd,rs1_current)
        if(prev_rd==rs1_current):
            return True
        else: 
            return False
    def pipeline_implementation(self,prev_instruction,Branch_flag=False):
        if(prev_instruction.F_starting==-1 or prev_instruction.D_starting==-1): return

        if(Branch_flag==False):
            self.F_starting=prev_instruction.D_starting
            self.F_ending=prev_instruction.D_ending
            if(prev_instruction.Ex==-1):
                return 
            self.D_starting=prev_instruction.Ex
            # if(prev_instruction.binary[25:]=="0000011" or prev_instruction.binary[25:]=="0100011" ):
            if True:
                if(self.check_hazard(prev_instruction)):
                    print("here")
                    self.D_ending=prev_instruction.Mem
                else:
                    self.D_ending=prev_instruction.Ex

            elif(prev_instruction.binary[25:]=="1100011"):
                self.D_ending=self.D_starting
                return
            else:
                self.D_ending=prev_instruction.Ex
            self.Ex=self.D_ending+1
            self.Mem=self.Ex+1
            self.Wr=self.Mem+1
            
        else:
            self.F_starting=prev_instruction.Ex+1
            self.F_ending=self.F_starting
            self.D_starting=self.F_ending+1
            self.D_ending=self.D_starting
            self.Ex=self.D_ending+1
            self.Mem=self.Ex+1
            self.wr=self.Mem+1

# class CPU:
#     def _init_(self,imem,mem1024):
#         self.imem = imem
#         self.fetch = Fetch(imem)
#         self.decode = Decode(self.imem,reg_val)
#         self.exec = Execute(opcode_to_instr,self.imem)             
#         self.memory = Memory(mem1024)
#         self.write = Writeback()

#         self.list_of_instr=imem.list_of_instr
#         self.cycles=self.list_of_instr[-1].Wb


    
#     def typeof(self,inst):
#       #print(inst)
#       if(inst[25:30]=="00000" or inst[25:30]=="01000"):
#         return 0
#       elif (inst[25:30]=="11000"):
#         return 2
#       else:
#         return 1

    
#     def execute(self):
#         ins=0
#         jmp=0
#         file1= open("drive/MyDrive/CA_test/log.txt","w")
#         for i in range(self.cycles):
#             if(ins>=len(self.l)):
#               break
#             curr_inst=self.l[ins]
#             if(self.typeof(curr_inst.instr)==1):
#               temp=curr_inst.x_start
#             elif(self.typeof(curr_inst.instr)==2):
#               temp=curr_inst.x_start
#               offset=curr_inst.instr[0]+curr_inst.instr[24]+curr_inst.instr[1:7]+curr_inst.instr[20:24]
#               offset=int(offset,2)
#               jmp=offset
#             elif(ins>0 and self.typeof(curr_inst.instr)==0 and is_in_use(self.l[ins-1].instr,curr_inst.instr)):
#               temp=curr_inst.m_start
#             elif(self.typeof(curr_inst.instr)==0):
#               temp=curr_inst.x_start
#             if(i==temp):
#               if(jmp==0):
#                 self.F.execute(ins,self.imem)
#                 self.D.decode(self.F,ins)
#                 self.X.execute(self.D,ins)
#                 #if(ins==1):
#                   #pdb.set_trace()
#                 self.M.execute(self.X)
#                 self.W.execute(self.M)
#                 ins+=1
#               else:
#                 self.F.execute(ins,self.imem)
#                 self.D.decode(self.F,ins)
#                 self.X.execute(self.D,ins)
#                 self.M.execute(self.X)
#                 self.W.execute(self.M)
#                 ins=jmp
#                 jmp=0
#             string="Clock cycle -"+str(i)+"\n"
#             file1.write(string)
#             ls=self.dmem.RF
#             for k in ls:
#               string=str(k)+"\n"
#               file1.write(string)
#             file1.write("\n")
#             print(self.dmem.RF)

#         for j in range(i,self.cycles+1):
#           print(self.dmem.RF)  
#           #print(self.cycles)

#         print(mem_reg)

#         file1.write("final data memory state \n")
#         ls=self.dmem.RF
#         for k in ls:
#           string=str(k)+"\n"
#           file1.write(string)
#         file1.write("\n")
#         file1.write("instruction memory state \n")
#         ls=self.imem.memory
#         for k in ls:
#           string=str(k)+"\n"
#           file1.write(string)
#         file1.write("\n")
#         file1.close()

def pipeline_show(instructions):
    for i in range(0, len(instructions)):
        obj = instructions[i]
        str_line = " " * obj.F_starting
        print()
        if obj.F_starting == -1:
            str_line = "- " * 5
            print(str_line)
            continue
        str_F = "F" * (obj.F_ending - obj.F_starting + 1)
        str_line += str_F
        if obj.D_starting == -1:
            str_line += "- " * 4
            print(str_line)
            continue
        str_D = "D" * (obj.D_ending - obj.D_starting + 1)
        str_line += str_D
        if obj.Ex == -1:
            str_line += "- " * 3
            print(str_line)
            continue
        str_X = "X"
        str_line += str_X
        str_M = "M"
        str_line += str_M
        str_W = "W"
        str_line += str_W
        print(str_line)


def main():
    instruct_mem = Instruction_Memory()
    PC = 0
    instructions = instruct_mem.list_of_instr()
    instruct_mem.initialize()
    num_instruction = instruct_mem.get_len()
    
    # Create a list to store the instances of the Instruction class
    instruction_list = []

    for PC in range(0, num_instruction):
        get_instrct = instruct_mem.getData(PC)
        Instruct_clas = Instruction(get_instrct)
        instruction_list.append(Instruct_clas)

    # Set the attributes for the first instruction
    instruction_list[0].F_starting = 0
    instruction_list[0].F_ending = 0
    instruction_list[0].D_starting = 1
    instruction_list[0].D_ending = 1
    instruction_list[0].Ex = 2
    instruction_list[0].Mem = 3
    instruction_list[0].Wr = 4

    jump = -1
    prev_PC = -1
    for PC in range(1, num_instruction):
        if instructions[PC][25:] == "1100011":
            immediate = int(
                instructions[PC][0]
                + instructions[PC][24]
                + instructions[PC][1:7]
                + instructions[PC][20:24],
                2,
            )

            jump = immediate
            prev_PC = PC
        if jump == PC:
            instruction_list[PC].pipeline_implementation(instruction_list[prev_PC], True)
        else:
            instruction_list[PC].pipeline_implementation(instruction_list[PC - 1])
    
    # Pass the list of instruction objects to the pipeline_show function
    pipeline_show(instruction_list)

main()



















# def __main__():
#     IM = Instruction_Memory()
#     no_instr = IM.initialize()
#     PC = 0
    
#     print(no_instr)
#     memory1024 = [random.randint(0, 255) for _ in range(1024)]
#     end=0

#     pipeline_arr = [0, 0, 0, 0, 0]
#     no_instr=5
#     end=0
#     i = 0
#     stage = {}
#     for i in range(no_instr):
#         stage[i] = "F"
#     cycle=0
    
#     while end == 0:
#         # for i in range(no_instr):
          
#         # print("\n")
#         print("Cycle",cycle)
#         cycle+=1
#         for i in range(0,len(stage)):
#             print(i, stage[i])

#         for i in range(no_instr):
#             # instruc = inst_mem.getData(i)
#             if stage[i] == "F" and pipeline_arr[0] == 0:

#                 pipeline_arr[0] = 1
#                 stage[i] = "D"

#             elif stage[i] == "D" and pipeline_arr[1] == 0:
#                 # decode
#                 pipeline_arr[1] = 1
#                 stage[i] = "X"

#             elif stage[i] == "X" and pipeline_arr[2] == 0:
#                 # execute
#                 pipeline_arr[2] = 1
#                 stage[i] = "M"

#             elif stage[i] == "M" and pipeline_arr[3] == 0:
#                 # memory
#                 pipeline_arr[3] = 1
#                 stage[i] = "W"

#             elif stage[i] == "W" and pipeline_arr[4] == 0:

#                 pipeline_arr[4] = 1
#                 # writeback
#                 stage[i] = ""
          
#             if stage[no_instr - 1] == "W":
#                 end = 1
#         pipeline_arr=[0,0,0,0,0]
#         print("\n")
#     print("Cycle",cycle)
#     for i in range(0,len(stage)):
#       print(i, stage[i])

# __main__()

#     def execute(self):
#         ins=0
#         jmp=0
#         file1= open("drive/MyDrive/CA_test/log.txt","w")
#         for i in range(self.cycles):
#             if(ins>=len(self.l)):
#               break
#             curr_inst=self.l[ins]
#             if(self.typeof(curr_inst.instr)==1):
#               temp=curr_inst.x_start
#             elif(self.typeof(curr_inst.instr)==2):
#               temp=curr_inst.x_start
#               offset=curr_inst.instr[0]+curr_inst.instr[24]+curr_inst.instr[1:7]+curr_inst.instr[20:24]
#               offset=int(offset,2)
#               jmp=offset
#             elif(ins>0 and self.typeof(curr_inst.instr)==0 and is_in_use(self.l[ins-1].instr,curr_inst.instr)):
#               temp=curr_inst.m_start
#             elif(self.typeof(curr_inst.instr)==0):
#               temp=curr_inst.x_start
#             if(i==temp):
#               if(jmp==0):
#                 self.F.execute(ins,self.imem)
#                 self.D.decode(self.F,ins)
#                 self.X.execute(self.D,ins)
#                 #if(ins==1):
#                   #pdb.set_trace()
#                 self.M.execute(self.X)
#                 self.W.execute(self.M)
#                 ins+=1
#               else:
#                 self.F.execute(ins,self.imem)
#                 self.D.decode(self.F,ins)
#                 self.X.execute(self.D,ins)
#                 self.M.execute(self.X)
#                 self.W.execute(self.M)
#                 ins=jmp
#                 jmp=0
#             string="Clock cycle -"+str(i)+"\n"
#             file1.write(string)
#             ls=self.dmem.RF
#             for k in ls:
#               string=str(k)+"\n"
#               file1.write(string)
#             file1.write("\n")
#             print(self.dmem.RF)

#         for j in range(i,self.cycles+1):
#           print(self.dmem.RF)  
#           #print(self.cycles)

#         print(mem_reg)

#         file1.write("final data memory state \n")
#         ls=self.dmem.RF
#         for k in ls:
#           string=str(k)+"\n"
#           file1.write(string)
#         file1.write("\n")
#         file1.write("instruction memory state \n")
#         ls=self.imem.memory
#         for k in ls:
#           string=str(k)+"\n"
#           file1.write(string)
#         file1.write("\n")
#         file1.close()



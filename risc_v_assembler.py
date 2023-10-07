import sys

input = sys.stdin.read().split("\n")[:-1]
instructions = []
for i in input:
    instructions.append(i.split())

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

def main(instructions):
    for i in instructions:
        if(type_dict[i[0]]=="U"):
            U_type(i)
        elif(type_dict[i[0]]=="UJ"):
            UJ_type(i)
        elif(type_dict[i[0]]=="I"):
            I_type(i)
        elif(type_dict[i[0]]=="R"):
            R_type(i)
        elif(type_dict[i[0]]=="S"):
            S_type(i)
        elif(type_dict[i[0]]=="SB"):
            SB_type(i)
        
# def U_type(i):




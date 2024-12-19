from pathlib import Path
import os
import re


ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
groups = re.split("\n\n", lines)

print(len(groups))
Register, Program = groups
print(Register)
print(Program)

register_list = Register.split()
print(register_list)
A, B, C = int(register_list[2]), int(register_list[5]), int(register_list[8])
# instruction pointer
ptr = 0
program = list(map(int, Program.split()[1].split(",")))
L = len(program)
print(program)

output_list = []

def combo(operand):
    match operand:
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _: # 0, 1, 2, 3
            return operand

def instructions(opcode, operand):
    global A, B, C, ptr
    match opcode:
        case 0: # adv
            A //= (2 ** combo(operand))
        case 1: # bxl
            B ^= operand
        case 2: # bst
            B = combo(operand) % 8
        case 3: # jnz
            if A != 0:
                ptr = operand
            else:
                ptr += 2
        case 4: # bxc
            B ^= C
        case 5: # out
            output_list.append(combo(operand) % 8)
        case 6: # bdv
            B = A // (2 ** combo(operand))
        case 7: # cdv
            C = A // (2 ** combo(operand))


while ptr + 1 < L:
    opcode, operand = program[ptr], program[ptr + 1]
    instructions(opcode, operand)
    print(ptr, output_list)
    if opcode != 3:
        ptr += 2

ans = ','.join(map(str, output_list))
print("ans ", ans) # 3,5,0,1,5,1,5,1,0
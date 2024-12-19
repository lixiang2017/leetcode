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
print("program: ", program)

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
    global A, B, C, ptr, output_list
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

def one_try(a):
    global A, B, C, ptr, output_list, L
    A = a
    # reset all
    ptr = 0
    B = C = 0
    output_list = []
    # start
    while ptr + 1 < L:
        opcode, operand = program[ptr], program[ptr + 1]
        instructions(opcode, operand)
        if opcode != 3:
            ptr += 2
        if len(output_list) >= L:
            return output_list
    return output_list


def solve():
    digits = [0] * L
    previous_start = [0] * L
    current_index = L - 1
    while current_index >= 0:
        a = sum(x * (8 ** i) for i, x in enumerate(digits))
        found_digit = False
        for j in range(previous_start[current_index] + 1, 8):
            output_list = one_try(a + j * 8 ** current_index)
            if output_list[current_index] != program[current_index]:
                continue
            # found a valid digit
            digits[current_index] = j
            previous_start[current_index] = j
            found_digit = True
            break
        if not found_digit:
            digits[current_index] = 0
            digits[current_index + 1] = 0
            previous_start[current_index] = 0
            current_index += 1
        else:
            current_index -= 1

    total = sum(x * (8 ** i) for i, x in enumerate(digits))
    print("total: ", total)

# solve() # total:  113151776532890 # wrong, too high
print(one_try(113151776532890))  # wrong
print(one_try(107413700225434))  # right

from pathlib import Path
import os
import re
import itertools
from collections import defaultdict

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
        # print(ptr, output_list)
        if opcode != 3:
            ptr += 2
        if len(output_list) > L:
            return False
        
    # print("output_list ", output_list)
    return output_list == program

# 8-th, octonary [octal] number system # good for input3
total = sum(x * (8 ** (i + 1)) for i, x in enumerate(program))
print("total: ", total) # 119135517790992
# 119135517790992 too high


x = 3 * 8 ** 15 + 5 * 8 ** 14 + 5 * 8 ** 13 + 6 * 8 ** 12 + 4 * 8 ** 11  + 4 * 8 ** 10
x += 6 * 8 ** 9 + 3 * 8 ** 8 
x += 3 * 8 ** 7 + 4 * 8 ** 6 + 4 * 8 ** 5
x += 2 * 8 ** 4
x += 4 * 8 ** 3 + 6 * 8 ** 2 
x += 3 * 8 ** 1 + 2 * 8 ** 0


def permutes():
    for p1 in range(1, 8):
        for p in itertools.product(range(8), repeat=15):
            pp = (p1, ) + p
            yield pp

ans = 8 ** 17
for p in permutes():
    # for a in range(x , x + 1): 
    a = sum(pp * i ** 8 for pp, i in zip(p, range(15, -1, -1)))
    print("trying ", a)
    if one_try(a):
        print("yes")
        print("found one ", a)
        ans = min(ans, a)
        print(output_list)
        break


# def one_try_for_each_number(a, i):
#     global A, B, C, ptr, output_list, L
#     A = a
#     # reset all
#     ptr = 0
#     B = C = 0
#     output_list = []
#     # start
#     while ptr + 1 < L:
#         opcode, operand = program[ptr], program[ptr + 1]
#         instructions(opcode, operand)
#         # print(ptr, output_list)
#         if opcode != 3:
#             ptr += 2
#         if len(output_list) > L:
#             return False
        
#     # print("output_list ", output_list)
#     return i < len(output_list) and output_list[i] == program[i]

# # possible digits for each number
# possible = defaultdict(list)
# for i in range(16):
#     for d in range(8):
#         a = d * 8 ** i
#         if one_try_for_each_number(a, i):
#             possible[i].append(d)
        
# print(possible)
# # defaultdict(<class 'list'>, {0: [1], 2: [2], 3: [4, 6, 7], 5: [4, 6, 7], 6: [2], 9: [2], 10: [4, 6, 7], 11: [4, 6, 7], 12: [3], 13: [5], 14: [5], 15: [3]})
# x = 0
# for i in range(16):
#     x += possible[i][0] * 8 ** i
# print(one_try(x))

# ans = ','.join(map(str, output_list))
print("ans ", ans) 
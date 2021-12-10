
def get_acc(file_name):
    accumulator = 0
    instructions = []

    with open(file_name) as f:
        for line in f:
            line = line.strip()    
            action, op = line.split(' ')
            instr = [action, op[0], int(op[1:])]
            instructions.append(instr)

    seen_idx = set()
    i = 0
    while True:
        if i in seen_idx:
            break

        seen_idx.add(i)
        action, operator, operand = instructions[i]
        if action == 'nop':
            i += 1
        elif action == 'acc':
            accumulator += operand * (1 if operator == '+' else -1)
            i += 1
        elif action == 'jmp':
            i += operand * (1 if operator == '+' else -1)

    print('accumulator: ', accumulator)
    return accumulator

c1 = get_acc('input1')
c = get_acc('input')

'''
accumulator:  5
accumulator:  1749
'''
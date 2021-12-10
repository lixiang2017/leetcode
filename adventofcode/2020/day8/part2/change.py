
def change(file_name):
    instructions = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()    
            action, op = line.split(' ')
            instr = [action, op[0], int(op[1:])]
            instructions.append(instr)

    n = len(instructions)

    def loopAcc():
        '''
        check every case
        return isLoop, accumulator_value
        isLoop = True, loop or idx is out of range
        '''
        # print(instructions)
        accumulator = 0
        seen_idx = set()
        i = 0
        while True:
            if i == n:
                break
            if i in seen_idx or i < 0 or i > n:
                return True, -1

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
        return False, accumulator        


    # try every jmp/nop
    for idx, instr in enumerate(instructions):
        action, operator, operand = instructions[idx]
        # if action in ['jmp', 'nop']:
        if action == 'nop':
            # change it to jmp
            instructions[idx][0] = 'jmp'
            isLoop, acc_value = loopAcc()
            if isLoop:
                # restore
                instructions[idx][0] = 'nop' 
            else:
                print('acc_value: ', acc_value)
                return acc_value           
        elif action == 'jmp':
            # change it to nop
            instructions[idx][0] = 'nop'  
            isLoop, acc_value = loopAcc()
            if isLoop:
                # restore
                instructions[idx][0] = 'jmp'     
            else:
                print('acc_value: ', acc_value)
                return acc_value

    print('error!')
    return



c1 = change('input1')
c = change('input')

'''
accumulator:  8
acc_value:  8
accumulator:  515
acc_value:  515
'''


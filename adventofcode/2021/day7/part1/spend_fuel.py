




def least_fuel(file_name):
    fuel = 0
    pos = []
    with open(file_name) as f:
        pos = list(map(int, f.readline().strip().split(',') )) 
    pos.sort()
    mid = len(pos) // 2
    for p in pos:
        fuel += abs(p - pos[mid])

    print('fuel: ', fuel)
    return fuel 


f1 = least_fuel('input1')
f = least_fuel('input')

'''
fuel:  37
fuel:  354129
'''

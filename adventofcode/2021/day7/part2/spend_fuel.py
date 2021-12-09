




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


def least_fuel2(file_name):
    fuel = 0
    pos = []
    with open(file_name) as f:
        pos = list(map(int, f.readline().strip().split(',') )) 
    pos.sort()
    # mid = len(pos) // 2
    avg = sum(pos) // len(pos)
    print('avg: ', avg)
    for p in pos:
        diff = abs(p - avg)
        fuel += (diff + 1) * diff // 2

    # avg - 1, avg + 1; left, right
    fuel_l = fuel_r = 0
    avg_l, avg_r = avg - 1, avg + 1
    for p in pos:
        diffl = abs(p - avg_l)
        fuel_l += (diffl + 1) * diffl // 2
        diffr = abs(p - avg_r)
        fuel_r += (diffr + 1) * diffr // 2

    print('fuel: ', fuel, 'fuel_l: ', fuel_l, 'fuel_r: ', 'fuel_r')
    f = min(fuel, fuel_l, fuel_r)
    print('f: ', f)
    return f 



f1 = least_fuel2('input1')
f = least_fuel2('input')

'''
avg:  4
fuel:  170 fuel_l:  183 fuel_r:  fuel_r
f:  168
avg:  494
fuel:  98905973 fuel_l:  98906973 fuel_r:  fuel_r
f:  98905973
'''

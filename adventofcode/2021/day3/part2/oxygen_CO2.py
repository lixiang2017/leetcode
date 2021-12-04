

report = []

with open('input') as f:
    for binary in f:
        binary = binary.strip()
        report.append(binary)

n = len(report)

def get_oxygen():
    filter_indice = list(range(n))
    for i in range(12):
        filter_indice_0 = [idx for idx in filter_indice if report[idx][i] == '0']
        filter_indice_1 = [idx for idx in filter_indice if report[idx][i] == '1']
        if len(filter_indice_1) >= len(filter_indice_0):
            filter_indice = filter_indice_1
        else:
            filter_indice = filter_indice_0
        if len(filter_indice) == 1:
            break
    return int(report[filter_indice[0]], 2)

def get_co2():
    filter_indice = list(range(n))
    for i in range(12):
        filter_indice_0 = [idx for idx in filter_indice if report[idx][i] == '0']
        filter_indice_1 = [idx for idx in filter_indice if report[idx][i] == '1']
        if len(filter_indice_1) >= len(filter_indice_0):
            filter_indice = filter_indice_0
        else:
            filter_indice = filter_indice_1
        if len(filter_indice) == 1:
            break
    return int(report[filter_indice[0]], 2)


oxy = get_oxygen()
co2 = get_co2()
print('oxy: ', oxy, 'co2: ', co2, 'product: ', oxy * co2)

'''
oxy:  3995 co2:  1696 product:  6775520
'''


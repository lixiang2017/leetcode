
import re 

required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')  # 'cid'
four_digits = r'^\d{4}$'
digit = r'^\d{2,3}$'
# 0-9 a -f
af09_6 = r'^[0-9a-f]{6}$'
d9 = r'^\d{9}$'

def check(passport):
    # print('check passport: ', passport)
    byr = passport['byr']
    iyr = passport['iyr']
    eyr = passport['eyr']
    hgt = passport['hgt']
    hcl = passport['hcl']
    ecl = passport['ecl']
    pid = passport['pid']

    if len(byr) != 4 or not re.match(four_digits, byr) or not 1920 <= int(byr) <= 2002:
        print('byr: ', byr)
        return False

    if len(iyr) != 4 or not re.match(four_digits, iyr) or not 2010 <= int(iyr) <= 2020 :
        print('iyr: ', iyr)
        return False

    if not re.match(four_digits, eyr) or not 2020 <= int(eyr) <= 2030:
        print('eyr: ', eyr)
        return False

    if len(hgt) < 2 or hgt[-2:] not in ('cm', 'in'):
        print('hgt1: ', hgt)
        return False
    if (hgt[-2:] == 'cm' and (not re.match(digit, hgt[: -2]) or not 150 <= int(hgt[: -2]) <= 193)) \
            or (hgt[-2:] == 'in' and (not re.match(digit, hgt[: -2]) or not 59 <= int(hgt[: -2]) <= 76) ): 
        print('hgt2: ', hgt)
        return False

    if len(hcl) != 7 or hcl[0] != '#' or not re.match(af09_6, hcl[1:]):
        print('hcl: ', hcl)
        return False

    if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        print('ecl: ', ecl)
        return False

    # if len(pid) != 9 or pid[0] != '0' or not re.match(d9, pid):
    if len(pid) != 9 or not re.match(d9, pid):
        print('pid: ', pid)
        return False

    return True

valid = 0
one_passport = dict()
with open('input') as f:
    for line in f:
        line = line.strip()
        if line == '':
            if len(one_passport) == 7:
                if check(one_passport):
                    valid += 1
                else:
                    print("---------------")
                    print('not valid passport: ', one_passport)
            # clear
            one_passport.clear()
        else:
            kvs = line.split(' ')
            for kv in kvs:
                k, v = kv.split(':')
                k, v = k.strip(), v.strip()
                if k in required:
                    one_passport[k] = v


print('valid: ', valid)

'''
valid:  186
'''
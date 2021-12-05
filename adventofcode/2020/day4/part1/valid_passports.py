

required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')  # 'cid'

valid = 0
one_passport = set()
with open('input') as f:
    for line in f:
        line = line.strip()
        if line == '':
            if len(one_passport) == 7:
                valid += 1
            # clear
            one_passport.clear()
        else:
            kvs = line.split(' ')
            for kv in kvs:
                k = kv.split(':')[0].strip()
                if k in required:
                    one_passport.add(k)



print('valid: ', valid)

'''
valid:  242
'''
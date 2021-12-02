

# horizontal, depth
h = d = 0
aim = 0
with open('input') as f:
    for line in f:
        direction, step = line.split()
        step = int(step)
        if direction == 'forward':
            h += step
            d += aim * step
        elif direction == 'up':
            aim -= step
        elif direction == 'down':
            aim += step

print('h: ', h, 'd: ', d)
print('product: ', h * d)


'''
python3 horizontal_depth.py
h:  1965 d:  1071386
product:  2105273490
'''

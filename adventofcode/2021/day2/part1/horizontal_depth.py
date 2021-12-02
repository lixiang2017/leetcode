
# horizontal, depth
h = d = 0
with open('input') as f:
    for line in f:
        direction, step = line.split()
        step = int(step)
        if direction == 'forward':
            h += step
        elif direction == 'up':
            d -= step
        elif direction == 'down':
            d += step

print('h: ', h, 'd: ', d)
print('product: ', h * d)

'''
python3 horizontal_depth.py
h:  1965 d:  1182
product:  2322630
'''
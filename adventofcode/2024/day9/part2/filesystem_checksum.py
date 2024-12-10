import os 


ans = 0
n = 0
with open(os.path.join(os.path.dirname(__file__), 'input'), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        # print(len(line)) # 19, 19999

n = len(line)
print(n)
left_file_id = 0
right_file_id = n // 2
i = 0
j = n - 1
block_pos = 0

# if space is taken
taken = [False] * n
# if file can be moved
can_move = [False] * n

# check each file, whether can be moved
# from right to left
for j in range(n - 1, 0, -2):
    file_id = j // 2
    file_size = int(line[j])
    # if j == 4:
    #     print(file_id, file_size)
    #     print(taken)
    # check space
    for i in range(1, j, 2):
        if not taken[i]:
            capacity = int(line[i])
        else:
            # remaining space
            capacity = taken[i][-1]
            
        if capacity >= file_size:
            # print("enough")
            if not taken[i]:
                taken[i] = [[file_id, file_size], capacity - file_size]
            else:
                taken[i].pop()
                taken[i] += [[file_id, file_size], capacity - file_size]
                
            can_move[j] = True
            break

# print(taken)

block_pos = 0
for i in range(n):
    # file
    if i % 2 == 0:
        if not can_move[i]:
            # left file blocks
            left_blocks = int(line[i])
            for block_index in range(block_pos, block_pos + left_blocks):
                left_file_id = i // 2
                ans += block_index * left_file_id
                # print("still ", block_index, left_file_id)
        
    # space
    else:
        if taken[i]:
            current_block_pos = block_pos
            for k in range(len(taken[i]) - 1):
                file_id, file_size = taken[i][k]
                # print("current_block_pos, file_id, file_size", current_block_pos, file_id, file_size)
                for block_index in range(current_block_pos, current_block_pos + file_size):
                    ans += block_index * file_id
                    # print("space ", block_index, file_id)
                current_block_pos += file_size
    
    block_pos += int(line[i])


print('ans: ', ans) # ans: 6307279963620
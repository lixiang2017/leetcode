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

right_blocks = 0
visited_j = set()

while i < j:
    # left file blocks
    left_blocks = int(line[i])
    for block_index in range(block_pos, block_pos + left_blocks):
        left_file_id = i // 2
        ans += block_index * left_file_id
        print("left ", block_index, left_file_id)
    
    block_pos += left_blocks
    
    # space: i + 1
    space_cnt = int(line[i + 1])

    while space_cnt > 0 and i < j:
        if j not in visited_j:
            right_blocks += int(line[j])
            visited_j.add(j)
        taken = min(space_cnt, right_blocks)
        
        for block_index in range(block_pos, block_pos + taken):
            right_file_id = j // 2
            ans += block_index * right_file_id
            print("right ", block_index, right_file_id)
        
        block_pos += taken
        
        if taken == space_cnt:
            # space is not enough
            space_cnt = 0
            right_blocks -= taken
            # i += 2
            break
        else:#  taken == right_blocks
            # space is enough
            space_cnt -= taken
            right_blocks -= taken
            j -= 2
    i += 2

print("i, j, right_blocks", i, j, right_blocks)
if i == j:
    for block_index in range(block_pos, block_pos + right_blocks):
        left_file_id = i // 2
        ans += block_index * left_file_id
        print("more left ", block_index, left_file_id)

print('ans: ', ans) # ans:  6291146824486
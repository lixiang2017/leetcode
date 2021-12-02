
nums = []

ans = 0
with open('input') as f:
    for x in f:
        nums.append(int(x))
        if len(nums) > 3 and nums[-1] > nums[-4]:
            ans += 1

print('ans: ', ans)

'''
python3 count_sliding_window.py
ans:  1158
'''
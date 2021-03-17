
import random

nums = []
for _ in range(20):
    nums.append(random.randint(0, 100))

print 'original array: ', nums

def bubbleSort(nums):
    N = len(nums)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

print 'sorted array: ', bubbleSort(nums)
if nums == sorted(nums):
    print 'right'
else:
    print 'wrong'

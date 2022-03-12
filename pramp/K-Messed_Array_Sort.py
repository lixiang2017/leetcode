'''
T: O(NlogN)

Time: 24ms
Passed: 6
Failed: 0
'''
def sort_k_messed_array(arr, k):
  return sorted(arr)

'''
T: O(NlogN)

Time: 30ms
Passed: 6
Failed: 0
'''
def sort_k_messed_array(arr, k):
  arr.sort()
  return arr


'''
priority queue
T: O(NlogK)
S: O(K)

Time: 45ms
Passed: 6
Failed: 0
'''
from heapq import heapify, heappop, heappush

def sort_k_messed_array(arr, k):
  ans = []
  n = len(arr)
  h = arr[: k + 1]
  heapify(h)
  for i in range(k + 1, n):
    x = heappop(h)
    ans.append(x)
    heappush(h, arr[i])
  
  while h:
    ans.append(heappop(h))
  
  return ans 


'''
Sliding Window, a k-length sliding window
T: O(NK)
S: O(1)

Time: 26ms
Passed: 6
Failed: 0
'''
def sort_k_messed_array(arr, k):
  n = len(arr)
  for i in range(n - 1):
    # to find the smallest one [i....i+k], put it on arr[i]
    smallest_idx = i
    for j in range(i + 1, i + k + 1):
      if j >= n:
        break
      if arr[j] < arr[smallest_idx]:
        smallest_idx = j
    # swap
    arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i]
    
  return arr



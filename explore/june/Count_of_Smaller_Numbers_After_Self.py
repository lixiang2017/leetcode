'''
Insert Sort
Time: O(NlogN)
Space: O(N)

62 / 65 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 0 minutes ago
Last executed input: [-10000,-10000,-10000,-10000,-10000,-9999,-9999,-9999,-9999,-9999,-9998,-9998,-9998,-9998,-9998,-9997,-
'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        smaller = []
        self.rear = []
        
        def insertSort(num):
            if not self.rear:
                self.rear.append(num)
                return 0
            
            l, r = 0, len(self.rear)
            pos = 0
            while l < r:
                mid = (r - l) // 2 + l
                if self.rear[mid] < num:
                    pos = mid + 1
                    l = mid + 1
                elif self.rear[mid] >= num:
                    pos = mid
                    r = mid
            self.rear = self.rear[: pos] + [num] + self.rear[pos: ]
            return pos
            
        for num in nums[:: -1]:
            smaller.append(insertSort(num))

        return smaller[:: -1]

'''
priority queue + Greedy
T: O(NlogN)
S: O(N)

Runtime: 754 ms, faster than 85.13% of Python3 online submissions for Course Schedule III.
Memory Usage: 20.1 MB, less than 29.29% of Python3 online submissions for Course Schedule III.
'''
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        h = []
        ans = 0
        current_total = 0
        for duration, lastday in courses:
            if current_total + duration <= lastday:
                current_total += duration 
                heappush(h, -duration)
            else:
                if h and current_total + h[0] + duration <= lastday and -h[0] > duration:
                    current_total = current_total + h[0] + duration 
                    heappop(h)
                    heappush(h, -duration)
            ans = max(ans, len(h))
    
        return ans

    
'''
[[100,200],[200,1300],[1000,1250],[2000,3200]]
[[1,2]]
[[3,2],[4,3]]
[[5,5],[4,6],[2,6]]


## 必须要 -h[0] > duration，更换才有价值。否则是买椟还珠
Input
[[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
Output
3
Expected
4
'''



'''
Runtime: 997 ms, faster than 48.29% of Python3 online submissions for Course Schedule III.
Memory Usage: 20.1 MB, less than 29.29% of Python3 online submissions for Course Schedule III.
'''
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        h = []
        ans = 0
        current_total = 0
        for duration, lastday in courses:
            if current_total + duration <= lastday:
                current_total += duration 
                heappush(h, -duration)
            elif h and -h[0] > duration:
                # current_total + h[0] + duration <= lastday, 
                # 不加这一条，不影响答案。因为只是替换，不影响len(h)
                # 但是，会降低速度
                current_total = current_total + h[0] + duration 
                heappop(h)
                heappush(h, -duration)
            ans = max(ans, len(h))
    
        return ans

'''
heappushpop(h, -duration)
return len(h)

Runtime: 960 ms, faster than 51.26% of Python3 online submissions for Course Schedule III.
Memory Usage: 20.1 MB, less than 29.29% of Python3 online submissions for Course Schedule III.
'''
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        h = []
        current_total = 0
        for duration, lastday in courses:
            if current_total + duration <= lastday:
                current_total += duration 
                heappush(h, -duration)
            elif h and -h[0] > duration:
                current_total = current_total + h[0] + duration 
                heappushpop(h, -duration)
        return len(h)




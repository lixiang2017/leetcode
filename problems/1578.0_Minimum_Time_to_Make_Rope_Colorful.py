'''
Maintain the running sum and max value for repeated letters.
T: O(N)
S: O(1)

Runtime: 2818 ms, faster than 21.32% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 25.2 MB, less than 7.17% of Python3 online submissions for Minimum Time to Make Rope Colorful.
'''
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        # consecutive
        max_need = 0
        total = 0
        for i, c in enumerate(colors):  
            if i == 0 or colors[i - 1] != c:   # find a new segment
                # remove, just keep max
                ans += total - max_need
                # for next round
                max_need = neededTime[i]
                total = neededTime[i]
            else: # the same segment
                max_need = max(max_need, neededTime[i])
                total += neededTime[i]
        # last segment 
        if len(colors) > 1 and colors[-1] == colors[-2]:
            ans += total - max_need
        return ans 
        

'''
Runtime: 3090 ms, faster than 11.09% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 25.1 MB, less than 12.42% of Python3 online submissions for Minimum Time to Make Rope Colorful.
'''
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # totalTime: total time needed to make rope colorful;
        # currMaxTime: maximum time of a balloon needed in this group 
        total_time = curr_max_time = 0
        
        # For each balloon in the array:
        for i in range(len(colors)):
            # If this balloon is the first balloon of a new group 
            # set the curr_max_time as 0.
            if i > 0 and colors[i] != colors[i - 1]:
                curr_max_time = 0
            
            # Increment total _time by the smaller one.
            # Update curr_max_time as the larger one.
            total_time += min(curr_max_time, neededTime[i])
            curr_max_time = max(curr_max_time, neededTime[i])
        
        # Return total_time as the minimum removal time.
        return total_time
        
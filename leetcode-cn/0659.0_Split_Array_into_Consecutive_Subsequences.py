class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        end_cnt = Counter()
        for x in nums:
            if cnt[x] > 0:
                if end_cnt[x - 1] > 0:
                    cnt[x] -= 1
                    end_cnt[x - 1] -= 1
                    end_cnt[x] += 1
                elif cnt[x + 1] > 0 and cnt[x + 2] > 0:
                    cnt[x] -= 1
                    cnt[x + 1] -= 1
                    cnt[x + 2] -= 1
                    end_cnt[x + 2] += 1
                else:
                    return False
        return True

'''
heapq
'''
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prev_length = heapq.heappop(queue)
                heapq.heappush(mp[x], prev_length + 1)
            else:
                heapq.heappush(mp[x], 1)
                
        return not any(queue and queue[0] < 3 for queue in mp.values())
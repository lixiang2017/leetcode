'''
44 / 66 个通过测试用例
状态：超出时间限制
'''
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        cut = sorted(set([start for start, end, _ in segments] + [end for start, end, _ in segments]))
        # print(cut)
        seg2color = defaultdict(set)
        
        for start, end, color in segments:   
            left = bisect.bisect_left(cut, start)
            right = bisect.bisect_left(cut, end)
            if start != cut[left]:
                seg2color[(start, cut[left])].add(color)
            while left < right and left + 1 < len(cut):
                seg2color[(cut[left], cut[left + 1])].add(color)
                left += 1
            if end != cut[right]:
                seg2color[(cut[right], end)].add(color)
            
        ans = []
        for interval, colors in seg2color.items():
            ans.append(list(interval) + [sum(colors)])
        return ans


'''
46 / 66 个通过测试用例
状态：超出时间限制
'''
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        cut = sorted(set([start for start, end, _ in segments] + [end for start, end, _ in segments]))
        # print(cut)
        seg2color = defaultdict(int)
        
        for start, end, color in segments:   
            left = bisect.bisect_left(cut, start)
            right = bisect.bisect_left(cut, end)
            if start != cut[left]:
                seg2color[(start, cut[left])] += color
            while left < right and left + 1 < len(cut):
                seg2color[(cut[left], cut[left + 1])] += color
                left += 1
            if end != cut[right]:
                seg2color[(cut[right], end)] += color
        
        return [list(interval) + [color] for interval, color in seg2color.items()]

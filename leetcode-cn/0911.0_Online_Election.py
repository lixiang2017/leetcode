'''
Binary Search

执行用时：384 ms, 在所有 Python3 提交中击败了76.15% 的用户
内存消耗：20.5 MB, 在所有 Python3 提交中击败了11.93% 的用户
通过测试用例：97 / 97
'''
'''
# sort, count -> person list
1: y o g
2: y o g
3: o g y
4: g y
5: g
6: g
'''

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # (time, win_persion_no) list
        self.time_person = []
        # count -> person list
        self.c2ps = defaultdict(list)
        # count for every person
        self.c = defaultdict(int)
        # leading count
        self.max_c = 0
        for p, t in zip(persons, times):
            self.c[p] += 1
            cnt = self.c[p]
            self.c2ps[cnt].append(p)
            if cnt > self.max_c:
                self.max_c = cnt 
            win_persion_no = self.c2ps[self.max_c][-1]
            self.time_person.append((t, win_persion_no))

        # print(self.time_person)
    def q(self, t: int) -> int:
        # idx = bisect_right(self.time_person, (t, float('inf')))
        idx = bisect_right(self.time_person, (t + 1, -1))
        return self.time_person[idx - 1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)


'''
执行用时：312 ms, 在所有 Python3 提交中击败了99.08% 的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了60.55% 的用户
通过测试用例：97 / 97
'''
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        tops = []
        top = -1
        voteCount = defaultdict(int)
        for p in persons:
            voteCount[p] += 1
            if voteCount[p] >= voteCount[top]:
                top = p 
            tops.append(top)
        self.tops = tops
        self.times = times

    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t) - 1
        return self.tops[idx]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)



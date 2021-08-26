'''
Sort+Two Pointers

执行用时：128 ms, 在所有 Python3 提交中击败了23.55% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了89.54% 的用户
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if l != r:
                t = people[l] + people[r]
            else:
                t = people[l]
            if t <= limit:
                boat += 1
                l += 1
                r -= 1
            else:
                boat += 1
                r -= 1

        return boat


'''
Sort+Two Pointers
while循环的等于有迷惑性.
当light == heavy时，说明现在就剩一个人，不管哪个判断，都不影响最后ans += 1，也就是为这一个人专门分配一只船

执行用时：116 ms, 在所有 Python3 提交中击败了49.56% 的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了17.30% 的用户
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        l, r = 0, len(people) - 1
        while l <= r:
            t = people[l] + people[r]
            if t <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boat += 1
        return boat

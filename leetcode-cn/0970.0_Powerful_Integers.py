'''
Time: O(log(bound/x) + log(bound/y) + log(bound/x) * log(bound/y))
Space: O(log(bound/x) + log(bound/y) + log(bound/x) * log(bound/y))

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了92.31%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了69.23%的用户
'''

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        xs = self.valuesWithinBounds(x, bound)
        ys = self.valuesWithinBounds(y, bound)
        if not xs:
            return []

        NX, NY = len(xs), len(ys)
        powerful = set()
        for i in range(NX):
            for j in range(NY):
                if xs[i] + ys[j] <= bound:
                    powerful.add(xs[i] + ys[j])
                else:
                    break

        return list(powerful)

    def valuesWithinBounds(self, x, bound):
        if bound < 1:
            return []
        if 1 == x:
            return [1]
        values = []
        power = 0
        while x ** power <= bound:
            values.append(x ** power)
            power += 1
        return values



'''
Time: O(log(bound) * log(bound))
Space: O(log(bound) * log(bound))

执行用时：40 ms, 在所有 Python 提交中击败了43.08%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了18.46%的用户

ref:
https://leetcode-cn.com/problems/powerful-integers/solution/qiang-zheng-shu-by-leetcode/
'''

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        powerful = set()
        # 2 ** 20 > bound
        for i in range(20):
            for j in range(20):
                v = x ** i + y ** j
                if v <= bound:
                    powerful.add(v)
        return list(powerful)
        


'''
ref:
https://leetcode-cn.com/problems/powerful-integers/comments/

执行用时：20 ms, 在所有 Python 提交中击败了84.62%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了12.31%的用户
'''
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        powerful = set()
        a = b = 1
        while a < bound:
            b = 1
            while a + b <= bound:
                powerful.add(a + b)
                if 1 == y:
                    break
                b *= y

            if 1 == x:
                break
            a *= x

        return list(powerful)







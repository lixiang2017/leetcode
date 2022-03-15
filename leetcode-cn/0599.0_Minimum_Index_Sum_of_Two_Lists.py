'''
hash table
T: O(M + N)
S: O(M)

执行用时：52 ms, 在所有 Python3 提交中击败了78.50% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了51.94% 的用户
通过测试用例：136 / 136
'''
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # common interest list for minimum index sum
        n1, n2 = len(list1), len(list2)
        index_sum, common = n1 + n2, []
        r2i = {restaurant: i for i, restaurant in enumerate(list1)}
        for i, restaurant in enumerate(list2):
            if restaurant in r2i:
                if r2i[restaurant] + i < index_sum:
                    index_sum = r2i[restaurant] + i
                    common = [restaurant]
                elif r2i[restaurant] + i == index_sum:
                    common.append(restaurant)

        return common 

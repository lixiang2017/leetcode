'''
Hash Table

执行用时：84 ms, 在所有 Python3 提交中击败了67.68% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了87.31% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(Counter(candyType)))


'''
Hash Set

执行用时：84 ms, 在所有 Python3 提交中击败了67.68% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了52.82% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))


'''
BitMap

执行用时：688 ms, 在所有 Python3 提交中击败了5.11% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了64.53% 的用户
通过测试用例：206 / 206
'''
import array
class BitMap:
    BITMASK = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
    BIT_CNT = [bin(i).count('1') for i in range(256)]
    
    def __init__(self, maxnum=0):
        nbytes = (maxnum + 7) // 8
        self.bitmap = array.array('B', [0 for i in range(nbytes)])

    def set(self, pos):
        self.bitmap[pos // 8] |= self.BITMASK[pos % 8]
    
    def count(self):
        return sum(self.BIT_CNT[x] for x in self.bitmap)

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        bm = BitMap(200001)
        for c in candyType:
            bm.set(c + 100000)
        return min(bm.count(), len(candyType) // 2)


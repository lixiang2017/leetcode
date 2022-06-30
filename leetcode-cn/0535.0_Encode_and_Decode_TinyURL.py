'''
hash table

执行用时：40 ms, 在所有 Python3 提交中击败了63.11% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了41.33% 的用户
通过测试用例：739 / 739
'''
class Codec:

    head = 'http://tinyurl.com/'
    # long -> short
    l2s = dict()
    # short -> long
    s2l = dict()
    idx = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.l2s:
            self.idx += 1
            self.l2s[longUrl] = self.head + str(self.idx)
            self.s2l[self.idx] = longUrl
        return self.l2s[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        tail_idx = int(shortUrl[len(self.head): ])
        return self.s2l[tail_idx]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


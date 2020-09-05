class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        l = len(s)
        dict = {}
        for i in range(l - 9):
            substr = s[i:i + 10]
            if substr in dict.keys():
      #     if dict.has_key(substr):                   #python2
                dict[substr] = dict[substr] + 1
            else:
                dict[substr] = 1

        list = []
        for key in dict.keys():
            if dict[key] > 1:
                list.append(key)

        return list


if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(s))
    assert (Solution().findRepeatedDnaSequences(s) == ["AAAAACCCCC", "CCCCCAAAAA"])


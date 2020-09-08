class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

def stringToCharArray(input):
    return json.loads(input)

def charArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToCharArray(line)
            
            ret = Solution().reverseString(s)

            out = charArrayToString(s)
            if ret is not None:
                print "Do not return anything, modify s in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
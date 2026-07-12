class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c = [], [], []
        for i, ch in enumerate(s):
            match ch:
                case "a":
                    a.append(i)
                case "b":
                    b.append(i)
                case "c":
                    c.append(i)

        if not a or not b or not c:
            return 0

        ans = i = j = k = 0
        an, bn, cn, n = len(a), len(b), len(c), len(s)
        for ch in s:
            match ch:
                case "a":
                    m = max(b[j], c[k])
                    ans += n - m
                    i += 1
                    if i >= an:
                        break

                case "b":
                    m = max(a[i], c[k])
                    ans += n - m
                    j += 1
                    if j >= bn:
                        break

                case "c":
                    m = max(a[i], b[j])
                    ans += n - m
                    k += 1
                    if k >= cn:
                        break

        return ans

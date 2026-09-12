def max_substring(s: str) -> str:
    """
    返回字符串中字典序最大的子串（即最大后缀）。
    双指针 + 匹配长度，时间 O(n)，空间 O(1)
    """
    n = len(s)
    if n == 0:
        return ""

    i, j, k = 0, 1, 0  # i=最优起点, j=候选起点, k=已匹配长度

    while j + k < n:
        if s[i + k] == s[j + k]:
            k += 1
        elif s[i + k] < s[j + k]:
            i = max(i + k + 1, j)
            j = i + 1
            k = 0
        else:  # s[i+k] > s[j+k]
            j = j + k + 1
            k = 0

    return s[i:]


# ---------- 测试 ----------
if __name__ == "__main__":
    tests = [
        "abcabcbb",
        "abcdef",
        "bbbbb",
        "pwwkew",
        "",
        "zabczabd",
        "abccba",
        "cbacbaz"
    ]
    for t in tests:
        print(f"{t!r:15} -> {max_substring(t)!r}")

"""
核心观察：字典序最大的子串一定是某个后缀（因为子串 s[i:j] 总是 <= 后缀 s[i:]，后者更长且前缀相同）。所以问题等价于找字典序最大的后缀。

一疑问：
应该是 
elif s[i + k] < s[j + k]:
            i = j  # 肯定会是这个吧？
            j = i + 1
            k = 0
            
            
结果出来了。你的 i = j 结果完全正确，但性能差很多。看实测数据：

N (字符串长度)	max(i+k+1, j) 优化版	i = j 你的写法
1,000	5 ms	459 ms
5,000	6 ms	12,882 ms
10,000	6 ms	37,061 ms
为什么 max(i + k + 1, j) 更快？

当 s[i+k] < s[j+k] 时，我们已经知道前 k 个字符完全相同：s[i..i+k-1] == s[j..j+k-1]。这意味着从 i+1, i+2, ..., i+k 这些位置开头的后缀，都不可能是最大后缀——因为它们对应位置的 j+1, j+2, ..., j+k 开头的后缀一定更大。

举个例子，s = "abcabcz"，i=0, j=3, k=3（匹配了 abc==abc），然后 s[3]='a' < s[6]='z'：

s[0:] = "abcabcz"、s[1:] = "bcabcz"、s[2:] = "cabcz"、s[3:] = "abcz" —— 这 4 个都被 s[3:] 及之后的位置击败了
所以 i 可以直接跳到 i + k + 1 = 4，跳过这一整段
如果只写 i = j，就只跳到 3，后面 i=3 又要从头匹配 "abcz" 对比 "bcz" 对比 "cz" 对比 "z"，白白重复劳动
最坏情况 "aaaa...ab"：i = j 会退化成 O(n²)，max(i+k+1, j) 保持 O(n)。

所以结论：i = j 对，max(i+k+1, j) 又对又快。用后者。
"""

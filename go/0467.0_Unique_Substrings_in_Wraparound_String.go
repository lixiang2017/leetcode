/*
执行用时：0 ms, 在所有 Go 提交中击败了100.00% 的用户
内存消耗：2.4 MB, 在所有 Go 提交中击败了90.24% 的用户
通过测试用例：81 / 81
*/
func findSubstringInWraproundString(p string) (ans int) {
    dp := [26]int{}
    k := 0
    for i, ch := range p {
        if i > 0 && (byte(ch) - p[i - 1] + 26) % 26 == 1 {
            k++
        } else {
            k = 1
        }
        dp[ch - 'a'] = max(dp[ch - 'a'], k)
    }
    for _, v := range dp {
        ans += v
    }
    return 
}   

func max(a, b int) int {
    if b > a {
        return b 
    }
    return a
}

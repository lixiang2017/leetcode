/*

执行用时：0 ms, 在所有 Go 提交中击败了100.00% 的用户
内存消耗：3.4 MB, 在所有 Go 提交中击败了100.00% 的用户
*/

func reverseStr(s string, k int) string {
    t := []byte(s)
    for i := 0; i < len(s); i += 2 * k {
        sub := t[i: min(i + k, len(s))]
        for j, n := 0, len(sub); j < n / 2; j++ {
            sub[j], sub[n - 1 - j] = sub[n - 1 - j], sub[j]
        }
    }
    return string(t)
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

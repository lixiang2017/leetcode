/*
Runtime: 2 ms, faster than 18.41% of Go online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 2 MB, less than 36.04% of Go online submissions for Find the Index of the First Occurrence in a String.
*/
func strStr(haystack string, needle string) int {
    m := len(needle)
    n := len(haystack)
    for windowStart := 0; windowStart <= n -m; windowStart++ {
        for i := 0; i < m; i++ {
            if needle[i] != haystack[windowStart + i] {
                break
            }
            if i == m - 1 {
                return windowStart
            }
        }
    }
    return -1
}

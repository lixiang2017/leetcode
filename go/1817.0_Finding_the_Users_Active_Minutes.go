/*
hash table

执行用时：124 ms, 在所有 Go 提交中击败了61.54% 的用户
内存消耗：9.3 MB, 在所有 Go 提交中击败了30.77% 的用户
通过测试用例：38 / 38
*/
func findingUsersActiveMinutes(logs [][]int, k int) []int {
    id2times := map[int]map[int]int{}
    for i := 0; i < len(logs); i++ {
        if id2times[logs[i][0]] == nil {
            id2times[logs[i][0]] = map[int]int{}
        }
        id2times[logs[i][0]][logs[i][1]]++
    }
    ans := make([]int, k)
    for _, v := range id2times {
        if len(v) - 1 < 0 {
            continue
        }
        ans[len(v) - 1]++
    }
    return ans 
}

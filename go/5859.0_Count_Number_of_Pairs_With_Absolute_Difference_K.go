/*
Brute Force

执行用时：8 ms, 在所有 Go 提交中击败了43.48% 的用户
内存消耗：3.1 MB, 在所有 Go 提交中击败了67.39% 的用户
通过测试用例：236 / 236
*/
func countKDifference(nums []int, k int) int {
    var count int
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j ++ {
            q := nums[i] - nums[j]
            if q < 0 {
                q = -q
            }
            if q == k {
                count++
            }
        }
    }
    return count
}

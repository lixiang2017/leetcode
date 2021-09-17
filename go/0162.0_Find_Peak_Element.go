/*
T: O(N)
S: O(1)

执行用时：0 ms, 在所有 Go 提交中击败了100.00% 的用户
内存消耗：2.7 MB, 在所有 Go 提交中击败了61.26% 的用户
通过测试用例：63 / 63
*/
func findPeakElement(nums []int) (idx int) {
    for i, v := range nums {
        if v > nums[idx] {
            idx = i
        }
    }
    return 
}

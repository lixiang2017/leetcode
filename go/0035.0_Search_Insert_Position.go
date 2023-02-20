/*
Runtime: 5 ms, faster than 59.16% of Go online submissions for Search Insert Position.
Memory Usage: 2.9 MB, less than 100.00% of Go online submissions for Search Insert Position.
*/
func searchInsert(nums []int, target int) int {
    left, right := 0, len(nums) - 1
    for left <= right {
        mid := (right - left) >> 1 + left
        if target <= nums[mid] {  // need mid, ie. right + 1, also ie. left
            right = mid - 1 
        } else {
            left = mid + 1
        }
    }
    return left     
}


/*
Runtime: 5 ms, faster than 59.16% of Go online submissions for Search Insert Position.
Memory Usage: 2.9 MB, less than 100.00% of Go online submissions for Search Insert Position.
*/
func searchInsert(nums []int, target int) int {
    left, right := 0, len(nums) - 1
    for left <= right {
        mid := (right - left) >> 1 + left
        if target <= nums[mid] {  // need mid, ie. right + 1, also ie. left
            right = mid - 1 
        } else {
            left = mid + 1
        }
    }
    return right + 1     
}

/*
Runtime: 8 ms, faster than 11.34% of C online submissions for Search Insert Position.
Memory Usage: 6.2 MB, less than 39.62% of C online submissions for Search Insert Position.
*/
int searchInsert(int* nums, int numsSize, int target){
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int mid = ((right - left) >> 1) + left;
        if (target <= nums[mid]) {  // need mid, ie. right + 1, also ie. left
            right = mid - 1; 
        } else {
            left = mid + 1;
        }
    }
    return left;   
}


/*
Runtime: 7 ms, faster than 42.88% of C online submissions for Search Insert Position.
Memory Usage: 6.2 MB, less than 39.62% of C online submissions for Search Insert Position.
*/
int searchInsert(int* nums, int numsSize, int target){
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int mid = ((right - left) >> 1) + left;
        if (target <= nums[mid]) {  // need mid, ie. right + 1, also ie. left
            right = mid - 1; 
        } else {
            left = mid + 1;
        }
    }
    return right + 1;   
}

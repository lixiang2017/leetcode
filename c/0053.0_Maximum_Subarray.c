/*
Success
Details
Runtime: 4 ms, faster than 98.67% of C online submissions for Maximum Subarray.
Memory Usage: 6.3 MB, less than 76.39% of C online submissions for Maximum Subarray.
*/

int maxSubArray(int* nums, int numsSize){
    int best_sum = - 1e5 - 2;
    int current_sum = - 1e5 - 2;
    for (int i = 0; i < numsSize; i++) {
        current_sum = fmax(current_sum + nums[i], nums[i]);
        best_sum = fmax(current_sum, best_sum);
    }
    return best_sum;
}

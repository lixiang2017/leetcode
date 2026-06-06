/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* leftRightDifference(int* nums, int numsSize, int* returnSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i++) {
        total += nums[i];
    }    

    int left_sum = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        nums[i] = abs(left_sum * 2 + x - total);
        left_sum += x;
    }
    *returnSize = numsSize;
    return nums;
}
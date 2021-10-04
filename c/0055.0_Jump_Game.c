/*
Runtime: 80 ms, faster than 45.73% of C online submissions for Jump Game.
Memory Usage: 8.6 MB, less than 35.81% of C online submissions for Jump Game.
*/

bool canJump(int* nums, int numsSize){
    int goal = numsSize - 1, i = 0;
    for (i = numsSize; i--; ) {
        if (i + nums[i] >= goal) {
            goal = i;
        }
    }
    return !goal;
}


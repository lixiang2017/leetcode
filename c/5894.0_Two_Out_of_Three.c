/*
执行用时：12 ms, 在所有 C 提交中击败了100.00% 的用户
内存消耗：6.4 MB, 在所有 C 提交中击败了100.00% 的用户
通过测试用例：288 / 288
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoOutOfThree(int* nums1, int nums1Size, int* nums2, int nums2Size, int* nums3, int nums3Size, int* returnSize){
    int cnt[3][101];
    int idx = 0;
    int *ans = (int*) malloc(sizeof(int) * 101);
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < nums1Size; ++i) {
        cnt[0][nums1[i]] = 1;
    }
    for (int i = 0; i < nums2Size; ++i) {
        cnt[1][nums2[i]] = 1;
    }
    for (int i = 0; i < nums3Size; ++i) {
        cnt[2][nums3[i]] = 1;
    }

    for (int i = 0; i < 101; ++i) {
        if (cnt[0][i] + cnt[1][i] + cnt[2][i] >= 2) {
            ans[idx++] = i;
        }
    }
    *returnSize = idx;
    return ans;
}

/*
执行用时：72 ms, 在所有 C++ 提交中击败了68.89% 的用户
内存消耗：57.5 MB, 在所有 C++ 提交中击败了86.44% 的用户
通过测试用例：60 / 60
*/

class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = 0;
        int i = 0, j = height.size() - 1;
        while (i < j) {
            ans = max(ans, min(height[i], height[j]) * (j - i));
            if (height[i] < height[j]) {
                ++i;
            } else {
                --j;
            }
        }
        return ans;
    }
};

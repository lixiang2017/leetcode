/*
摩尔投票法
T: O(N)
S: O(1)

执行用时：16 ms, 在所有 C++ 提交中击败了73.65% 的用户
内存消耗：19.2 MB, 在所有 C++ 提交中击败了38.79% 的用户
通过测试用例：47 / 47
*/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int element = 0, vote = 0;
        for (auto x: nums) {
            if (vote > 0 && x == element) {
                vote++;
            } else if (vote == 0) {
                element = x;
                vote = 1;
            } else {
                vote--;
            }
        }
        return element;
    }
};

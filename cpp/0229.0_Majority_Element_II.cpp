/*
执行用时：12 ms, 在所有 C++ 提交中击败了68.66% 的用户
内存消耗：15.3 MB, 在所有 C++ 提交中击败了82.08% 的用户
通过测试用例：82 / 82
*/

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> ans;
        int element1 = 0, element2 = 0;
        int vote1 = 0, vote2 = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (vote1 > 0 && nums[i] == element1) {
                vote1++;
            } else if (vote2 > 0 and nums[i] == element2) {
                vote2++;
            } else if (vote1 == 0) {
                element1 = nums[i];
                vote1 = 1;
            } else if (vote2 == 0) {
                element2 = nums[i];
                vote2 = 1;
            } else {
                vote1--;
                vote2--;
            }
        }

        int cnt1 = 0, cnt2 = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == element1) {
                cnt1++;
            } else if (nums[i] == element2) {
                cnt2++;
            }
        }
        if (cnt1 > nums.size() / 3) {
            ans.push_back(element1);
        }
        if (cnt2 > nums.size() / 3) {
            ans.push_back(element2);
        }
        return ans;
    }
};

/*
approach: multiset + Sliding Window
Time: O(NlogN)
Space: O(N)

ref:
https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/he-gua-de-shu-ju-jie-gou-hua-dong-chuang-v46j/

执行结果：
通过
显示详情
执行用时：232 ms, 在所有 C++ 提交中击败了66.00%的用户
内存消耗：76.6 MB, 在所有 C++ 提交中击败了23.14%的用户
*/



class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        multiset<int> st;
        int left = 0, right = 0, longest = 0;
        while (right < nums.size()) {
            st.insert(nums[right]);
            while (*st.rbegin() - *st.begin() > limit) {
                st.erase(st.find(nums[left]));
                left ++;
            }
            longest = max(longest, right - left + 1);
            right ++;
        }
        return longest;
    }
};

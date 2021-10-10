/*
执行用时：24 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：27.3 MB, 在所有 C++ 提交中击败了100.00% 的用户
通过测试用例：288 / 288
*/
class Solution {
public:
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
        unordered_set<int> us1 (nums1.begin(), nums1.end());
        unordered_set<int> us2 (nums2.begin(), nums2.end());
        unordered_set<int> us3 (nums3.begin(), nums3.end());

        unordered_set<int> us;
        us.insert(us1.begin(), us1.end());
        us.insert(us2.begin(), us2.end());
        us.insert(us3.begin(), us3.end());

        vector<int> ans;
        for (int x: us) {
            int f1 = us1.find(x) != us1.end() ? 1 : 0;
            int f2 = us2.find(x) != us2.end() ? 1 : 0;
            int f3 = us3.find(x) != us3.end() ? 1 : 0;
            if (f1 + f2 + f3 >= 2) {
                ans.push_back(x);
            }
        }
        return ans;
    }
};



/*
执行用时：20 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：27.2 MB, 在所有 C++ 提交中击败了100.00% 的用户
通过测试用例：288 / 288
*/
class Solution {
public:
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
        unordered_set<int> us1 (nums1.begin(), nums1.end());
        unordered_set<int> us2 (nums2.begin(), nums2.end());
        unordered_set<int> us3 (nums3.begin(), nums3.end());

        unordered_set<int> us;
        us.insert(nums1.begin(), nums1.end());
        us.insert(nums2.begin(), nums2.end());
        us.insert(nums3.begin(), nums3.end());

        vector<int> ans;
        for (int x: us) {
            int f1 = us1.find(x) != us1.end() ? 1 : 0;
            int f2 = us2.find(x) != us2.end() ? 1 : 0;
            int f3 = us3.find(x) != us3.end() ? 1 : 0;
            if (f1 + f2 + f3 >= 2) {
                ans.push_back(x);
            }
        }
        return ans;
    }
};

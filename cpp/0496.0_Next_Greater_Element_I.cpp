/*
Stack / Monotonic Stack
T: O(M + N)
S: O(M + 2N)

Runtime: 14 ms, faster than 22.65% of C++ online submissions for Next Greater Element I.
Memory Usage: 8.8 MB, less than 58.15% of C++ online submissions for Next Greater Element I.
*/
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> s;
        unordered_map<int, int> m;
        for (int n: nums2) {
            while (s.size() && s.top() < n) {
                m[s.top()] = n;
                s.pop();
            }
            s.push(n);
        }
        vector<int> ans;
        for (int n: nums1) ans.push_back(m.count(n) ? m[n]: -1);
        return ans;
    }
};


/*
Stack / Monotonic Stack
T: O(M + N)
S: O(M + 2N)

Runtime: 11 ms, faster than 30.83% of C++ online submissions for Next Greater Element I.
Memory Usage: 8.7 MB, less than 78.40% of C++ online submissions for Next Greater Element I.
*/
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int M = nums1.size();
        stack<int> s;
        unordered_map<int, int> m;
        for (int n: nums2) {
            while (s.size() && s.top() < n) {
                m[s.top()] = n;
                s.pop();
            }
            s.push(n);
        }
        vector<int> ans(M, -1);
        //for (int n: nums1) ans.push_back(m.count(n) ? m[n]: -1);
        for (int i = 0; i < M; i++) {
            auto itr = m.find(nums1[i]);
            if (itr != m.end()) {
                ans[i] = itr->second;
            }
        }
        return ans;
    }
};

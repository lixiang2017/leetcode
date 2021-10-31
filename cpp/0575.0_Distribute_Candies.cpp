/*
unordered_set

执行用时：196 ms, 在所有 C++ 提交中击败了74.92% 的用户
内存消耗：113.3 MB, 在所有 C++ 提交中击败了49.42% 的用户
通过测试用例：206 / 206
*/

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> s;
        for (auto c: candyType) {
            s.insert(c);
        }
        return min(candyType.size() / 2, s.size());
    }
};

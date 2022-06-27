/*
执行用时：20 ms, 在所有 C++ 提交中击败了91.86% 的用户
内存消耗：13.2 MB, 在所有 C++ 提交中击败了77.66% 的用户
通过测试用例：97 / 97
*/
class Solution {
public:
    int minPartitions(string n) {
        return *max_element(n.begin(), n.end()) - '0';
    }
};


/*
Runtime: 33 ms, faster than 81.14% of C++ online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
Memory Usage: 13.6 MB, less than 65.18% of C++ online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
*/
class Solution {
public:
    int minPartitions(string n) {
        char m = '1';
        for (auto ch: n) {
            m = max(m, ch);
            if (m == '9') {
                return 9;
            }
        }
        return m - '0';
    }
};

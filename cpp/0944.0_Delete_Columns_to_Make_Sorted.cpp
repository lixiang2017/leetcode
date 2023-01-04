/*
执行用时：36 ms, 在所有 C++ 提交中击败了68.31% 的用户
内存消耗：11.9 MB, 在所有 C++ 提交中击败了42.44% 的用户
通过测试用例：85 / 85
*/
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int ans = 0;
        for (int i = 0; i < strs[0].size(); ++i) {
            for (int j = 0; j < strs.size() - 1; ++j) {
                if (strs[j][i] > strs[j + 1][i]) {
                    ++ans;
                    break;
                }
            }
        }
        return ans;
    }
};


/*
Runtime: 47 ms, faster than 81.16% of C++ online submissions for Delete Columns to Make Sorted.
Memory Usage: 12.2 MB, less than 30.23% of C++ online submissions for Delete Columns to Make Sorted.
*/
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int K = strs[0].size();
        int answer = 0;
        // iterate over each index in the string
        for (int col = 0; col < K; col++) {
            for (int row = 1; row < strs.size(); row++) {
                if (strs[row][col] < strs[row - 1][col]) {
                    answer++;
                    break;
                }
            }
        }
        return answer;
    }
};

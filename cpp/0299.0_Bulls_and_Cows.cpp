/*
one pass

执行用时：8 ms, 在所有 C++ 提交中击败了19.28% 的用户
内存消耗：6.2 MB, 在所有 C++ 提交中击败了99.28% 的用户
通过测试用例：152 / 152
*/
class Solution {
public:
    string getHint(string secret, string guess) {
        vector<int> nums(10);
        int countA = 0, countB = 0;
        for (int i = 0; i < secret.size(); i++) {
            if (secret[i] == guess[i]) {
                countA++;
            } else {
                if (nums[guess[i] - '0']-- > 0) {
                    countB++;
                }
                if (nums[secret[i] - '0']++ < 0 ) {
                    countB++;
                }
            }
        }
        return to_string(countA) + "A" + to_string(countB) + "B";
    }
};

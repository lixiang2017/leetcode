/*
执行用时：4 ms, 在所有 C++ 提交中击败了40.65% 的用户
内存消耗：6 MB, 在所有 C++ 提交中击败了40.17% 的用户
通过测试用例：550 / 550
*/

class Solution {
public:
    bool detectCapitalUse(string word) {
        // upper case letter count
        int cnt = 0;
        for (auto w: word) {
            if (w >= 'A' && w <= 'Z') {
                cnt++;
            }
        }
        return (cnt == word.length()) || (cnt==1 && word[0]>='A' && word[0]<='Z') || cnt == 0;
    }
};

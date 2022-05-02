/*
执行用时0 m, 在所有 C++ 提交中击败100.00的用户
内存消耗6 M, 在所有 C++ 提交中击败100.00的用户
通过测试用例112 / 112
*/
class Solution {
public:
    string removeDigit(string number, char digit) {
        int t = 0;
        for (int i = 0; i < number.size(); i++) {
            if(number[i] == digit) {
                t = i;
                if (i + 1 < number.size() && number[i + 1] > digit) {
                    break;
                }
            }
        }
        return number.substr(0, t) + number.substr(t + 1);
    }
};


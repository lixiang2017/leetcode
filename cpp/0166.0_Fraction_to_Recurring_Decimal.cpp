/*
执行用时：4 ms, 在所有 C++ 提交中击败了40.50% 的用户
内存消耗：6.3 MB, 在所有 C++ 提交中击败了9.22% 的用户
通过测试用例：39 / 39
*/
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        long num = static_cast<long>(numerator);
        long den = static_cast<long>(denominator);
        string ans;
        if (num * den < 0) {
            ans += '-';
            num = abs(num);
            den = abs(den);
        }
        ans += to_string(num / den);
        num = (num % den) * 10;
        if (0 == num) return ans;
        ans += '.';

        unordered_map<long, int> rest2pos;
        int pos = ans.size(), rest = 0;
        bool cycle = false;
        while(num) {
            rest = num % den;
            if (rest2pos.count(rest) && ans[rest2pos[rest]] - '0' == num / den) {
                cycle = true;
                break;
            }
            rest2pos[rest] = pos++;
            ans.append(1, '0' + (num / den));
            num = (num % den) * 10;
        }
        if (cycle) {
            int pos = rest2pos[rest];
            ans = ans.substr(0, pos) + '(' + ans.substr(pos) + ')';
        }
        return ans;
    }
};

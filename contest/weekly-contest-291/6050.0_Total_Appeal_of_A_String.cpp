/*
DP 
from left to right

执行用时16 m, 在所有 C++ 提交中击败100.00的用户
内存消耗10.3 M, 在所有 C++ 提交中击败100.00的用户
通过测试用例76 / 76
*/
class Solution {
public:
    long long appealSum(string s) {
        vector<int> pos(26, -1);
        long long ans = 0, sum_g = 0;
        for (int i = 0; i < s.size(); i++) {
            int d = s[i] - 'a';
            sum_g += i - pos[d];
            ans += sum_g;
            pos[d] = i;
        }
        return ans;
    }
};


/*
DP 
from right to left

执行用时16 m, 在所有 C++ 提交中击败100.00的用户
内存消耗10.3 M, 在所有 C++ 提交中击败100.00的用户
通过测试用例76 / 76

0......i, i+1.....j....n-1
       c          c
往 s[i+1...n-1] 左侧加个字符s[i]
1、s[i+1...n-1] 从来没出现这个字符，sum_g 增加 (n - i)
2、s[i+1...n-1] 出现过这个字符，sum_g 增加 (pos[d] - i)
*/

class Solution {
public:
    long long appealSum(string s) {
        int n = s.size();
        vector<int> pos(26, n);
        long long ans = 0, sum_g = 0;
        for (int i = n - 1; i >= 0; i--) {
            int d = s[i] - 'a';
            sum_g += pos[d] - i;
            ans += sum_g;
            pos[d] = i;
        }
        return ans;
    }
};




/*
from left to right

执行用时16 m, 在所有 C++ 提交中击败100.00的用户
内存消耗10.3 M, 在所有 C++ 提交中击败100.00的用户
通过测试用例76 / 76
*/
class Solution {
public:
    long long appealSum(string s) {
        vector<int> pos(26, -1);
        long long ans = 0;
        int n = s.size();
        for (int i = 0; i < n; i++) {
            int d = s[i] - 'a';
            int left = i - pos[d];
            ans += left * (n - i);
            pos[d] = i;
        }
        return ans;
    }
};



/*
from right to left

执行用时20 m, 在所有 C++ 提交中击败100.00的用户
内存消耗10.3 M, 在所有 C++ 提交中击败100.00的用户
通过测试用例76 / 76
*/
class Solution {
public:
    long long appealSum(string s) {
        int n = s.size();
        vector<int> pos(26, n);
        long long ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            int d = s[i] - 'a';
            int right = pos[d] - i;
            ans += (i + 1) * right;
            pos[d] = i;
        }
        return ans;
    }
};


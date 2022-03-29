/*
执行用时：128 ms, 在所有 C++ 提交中击败了72.90% 的用户
内存消耗：120.8 MB, 在所有 C++ 提交中击败了31.61% 的用户
通过测试用例：64 / 64
*/
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int sum = mean * (n + m);
        vector<int> ans;

        for (int i = 0; i < m; i++) sum -= rolls[i];
        if (sum < n || sum > 6 * n) return ans;
        int remainder = sum % n, quotient = sum / n;
        for (int i = 0; i < n; i++) ans.push_back(quotient);
        for (int i = 0; i < remainder; i++) ans[i]++;
        return ans;    
    }
};


/*
执行用时：124 ms, 在所有 C++ 提交中击败了80.65% 的用户
内存消耗：120.8 MB, 在所有 C++ 提交中击败了23.87% 的用户
通过测试用例：64 / 64
*/
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int sum = mean * (n + m);
        vector<int> ans;

        for (int i = 0; i < m; i++) sum -= rolls[i];
        if (sum < n || sum > 6 * n) return ans;
        int remainder = sum % n, quotient = sum / n;
        for (int i = 0; i < remainder; i++) ans.push_back(quotient + 1);
        for (int i = remainder; i < n; i++) ans.push_back(quotient);
        return ans;    
    }
};


#define PB push_back

class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int sum = mean * (n + m);
        vector<int> ans;

        for (int i = 0; i < m; i++) sum -= rolls[i];
        if (sum < n || sum > 6 * n) return ans;
        int remainder = sum % n, quotient = sum / n;
        for (int i = 0; i < remainder; i++) ans.PB(quotient + 1);
        for (int i = remainder; i < n; i++) ans.PB(quotient);
        return ans;    
    }
};



/*
执行用时：116 ms, 在所有 C++ 提交中击败了93.55% 的用户
内存消耗：110.9 MB, 在所有 C++ 提交中击败了91.61% 的用户
通过测试用例：64 / 64
*/
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int left = mean * (rolls.size() + n) - accumulate(rolls.begin(), rolls.end(), 0);
        if (left < n || left > 6 * n) return {};
        vector<int> ans(n, left / n);
        for (int i = 0; i < left % n; i++) ans[i]++;
        return ans;
    }
};


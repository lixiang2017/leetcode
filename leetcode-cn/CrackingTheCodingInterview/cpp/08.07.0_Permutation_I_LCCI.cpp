/*
执行用时：8 ms, 在所有 C++ 提交中击败了99.70% 的用户
内存消耗：19.2 MB, 在所有 C++ 提交中击败了92.49% 的用户
通过测试用例：30 / 30
*/
class Solution {
public:
    vector<string> permutation(string S) {
        vector<string> ans;
        sort(S.begin(), S.end());
        ans.push_back(S);
        while (next_permutation(S.begin(), S.end())) {
            ans.push_back(S);
        }
        return ans;
    }
};


/*
执行用时：16 ms, 在所有 C++ 提交中击败了87.84% 的用户
内存消耗：19.2 MB, 在所有 C++ 提交中击败了92.94% 的用户
通过测试用例：30 / 30
*/
class Solution {
public:
    vector<string> permutation(string S) {
        vector<string> ans;
        sort(S.begin(), S.end());
        ans.push_back(S);
        while (nextPermutation(S)) {
            ans.push_back(S);
        }
        return ans;
    }

    bool nextPermutation(string& s) {
        int n = s.size();
        int i = n - 2;
        while (i >= 0 && s[i] >= s[i + 1])
            i--;
        if (i == -1)
            return false;
          
        int j = n - 1;
        while (j > i && s[i] >= s[j])
            j--;
        swap(s[i], s[j]);
        reverse(s.begin() + i + 1, s.end());
        return true;
    }
};


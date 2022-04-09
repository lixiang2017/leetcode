/*
hash table

执行用时：40 ms, 在所有 C++ 提交中击败了92.97% 的用户
内存消耗：20 MB, 在所有 C++ 提交中击败了56.93% 的用户
通过测试用例：36 / 36
*/
class Solution {
private:
    vector<int> freq;
public:
    Solution(): freq(26) {};

    int countCharacters(vector<string>& words, string chars) {
        int ans = 0;
        for (char ch: chars) {
            freq[ch - 'a']++;
        }

        auto check = [this](string& word) {
            vector<int> f(26);
            for (char ch: word) {
                int idx = ch - 'a';
                f[idx]++;
                if (f[idx] > this->freq[idx]) return false;
            }
            return true;
        };

        for (string &w: words) {
            if (check(w)) {
                ans += w.size();
            }
        }
        return ans;
    }
};


/*
执行用时：40 ms, 在所有 C++ 提交中击败了92.97% 的用户
内存消耗：19.8 MB, 在所有 C++ 提交中击败了60.72% 的用户
通过测试用例：36 / 36
*/
class Solution {
public:
    vector<int> freq = vector<int>(26);

    int countCharacters(vector<string>& words, string chars) {
        int ans = 0;
        for (char ch: chars) {
            freq[ch - 'a']++;
        }

        for (string &w: words) {
            if (check(w)) {
                ans += w.size();
            }
        }
        return ans;
    }

    bool check (string& word) {
        vector<int> f(26);
        for (char ch: word) {
            int idx = ch - 'a';
            f[idx]++;
            if (f[idx] > this->freq[idx]) return false;
        }
        return true;
    }
};



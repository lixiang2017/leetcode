/*
backtrack + freq

执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：12.5 MB, 在所有 C++ 提交中击败了17.95% 的用户
通过测试用例：175 / 175
*/

class Solution {
private:
    vector<pair<int, int>> freq;
    vector<vector<int>> ans;
    vector<int> sequence;

public:
    void backtrack(int pos, int rest) {
        if (0 == rest) {
            ans.push_back(sequence);
            return;
        }
        if (pos == freq.size() || rest < freq[pos].first) {
            return;
        }
        // not choose freq[pos]
        backtrack(pos + 1, rest);
        // choose freq[pos]
        int most = min(rest / freq[pos].first, freq[pos].second);
        for (int i = 1; i <= most; ++i) {
            sequence.push_back(freq[pos].first);
            backtrack(pos + 1, rest - i * freq[pos].first);
        }   
        for (int i = 1; i <= most; ++i) {
            sequence.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        for (int x: candidates) {
            if (freq.empty() || x != freq.back().first) {
                freq.emplace_back(x, 1);
            } else  {
                ++freq.back().second;
            }
        }
        backtrack(0, target);
        return ans;
    }
};


/*
backtrack + used list 

执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：14.5 MB, 在所有 C++ 提交中击败了10.53% 的用户
通过测试用例：175 / 175
*/
class Solution {
private:
    vector<vector<int>> ans;
    vector<int> sequence;
    int n = 110;
    vector<bool> used = vector<bool> (n, false);

public:
    void backtrack(int pos, int rest, vector<int>& candidates) {
        if (0 == rest) {
            ans.push_back(sequence);
            return;
        }
        if (pos == n || rest < candidates[pos]) {
            return;
        }
        // not choose [pos]
        backtrack(pos + 1, rest, candidates);
        // choose [pos]
        if (pos > 0 && candidates[pos - 1] == candidates[pos] && !used[pos - 1]) {
            return;
        }
        sequence.push_back(candidates[pos]);
        used[pos] = true;
        backtrack(pos + 1, rest - candidates[pos], candidates);
        sequence.pop_back();
        used[pos] = false;
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        n = candidates.size();
        backtrack(0, target, candidates);
        return ans;
    }
};

/*
执行用时：8 ms, 在所有 C++ 提交中击败了96.08% 的用户
内存消耗：11.6 MB, 在所有 C++ 提交中击败了5.55% 的用户
通过测试用例：103 / 103
*/

class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, string> m;
        for (auto p: paths) m[p[0]] = p[1];
        for (auto p: paths) {
            if (!m.count(p[1])) return p[1];
        }
        return "";   // need
    }
};


/*
执行用时：8 ms, 在所有 C++ 提交中击败了96.08% 的用户
内存消耗：11.3 MB, 在所有 C++ 提交中击败了11.44% 的用户
通过测试用例：103 / 103
*/
class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> citySet;
        for (auto p: paths) citySet.insert(p[1]);
        for (auto p: paths) {
            citySet.erase(p[0]);
        }
        return *citySet.begin();
    }
};



/*
执行用时：12 ms, 在所有 C++ 提交中击败了78.83% 的用户
内存消耗：11.3 MB, 在所有 C++ 提交中击败了11.08% 的用户
通过测试用例：103 / 103
*/
class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        set<string> citySet;
        for (auto p: paths) citySet.emplace(p[0]);
        for (auto p: paths) {
            if (citySet.find(p[1]) == citySet.end()) {
                return p[1];
            }
        }
        return "";
    }
};


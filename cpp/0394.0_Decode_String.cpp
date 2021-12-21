/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Decode String.
Memory Usage: 6.6 MB, less than 53.22% of C++ online submissions for Decode String.
*/

class Solution {
public:
    string nTimesString(string s, int n) {
        string ans = "";
        for (int i = 0; i < n; i++) {
            ans += s;
        }
        return ans;
    }
    
    string decodeString(string s) {
        vector<string> stack;
        string cur_string = "", cur_num = "";
        for (char ch: s) {
            if (ch == '[') {
                stack.push_back(cur_string);
                stack.push_back(cur_num);
                cur_string = "";
                cur_num = "";
            } else if (ch == ']') {
                string n = stack.back(); stack.pop_back();
                string prev_string = stack.back(); stack.pop_back();
                cur_string = prev_string + nTimesString(cur_string, stoi(n));
            } else if (isdigit(ch)) {
                cur_num += ch;
            } else {
                cur_string += ch;
            }
        }
        return cur_string;
    }
};

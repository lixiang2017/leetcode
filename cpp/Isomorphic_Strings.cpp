/*

You are here!
Your runtime beats 64.89 % of cpp submissions.
You are here!
Your memory usage beats 88.81 % of cpp submissions.
*/

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, char> s2t;
        unordered_map<char, char> t2s;
        for (int i = 0; i < s.size(); i++) {
            if (s2t.count(s[i]) == 0) {
                if (t2s.count(t[i]) != 0) {
                    return false;
                }
                s2t[s[i]] = t[i];
                t2s[t[i]] = s[i];                
            } else {
                if (s2t[s[i]] != t[i]) {
                    return false;
                }
            }   
        }
        return true;
    }
};



/*
You are here!
Your runtime beats 97.00 % of cpp submissions.
You are here!
Your memory usage beats 88.81 % of cpp submissions.
*/
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) return false;
        vector<int> m1(256, -1);
        vector<int> m2(256, -1);
        for (int i = 0; i < s.length(); i++) {
            if (m1[s[i]] != m2[t[i]]) return false;
            m1[s[i]] = i;
            m2[t[i]] = i;
        }
        return true;
    }
};




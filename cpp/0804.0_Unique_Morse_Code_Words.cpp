/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：8.3 MB, 在所有 C++ 提交中击败了66.35% 的用户
通过测试用例：82 / 82
*/
class Solution {
public:
    unordered_map<string, int> trans;
    int uniqueMorseRepresentations(vector<string>& words) {
        string morse[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
                            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                            "...","-","..-","...-",".--","-..-","-.--","--.."};
        for (auto w: words) {
            string t = "";
            for (auto ch: w) {
                t += morse[ch - 'a'];
            }
            trans[t]++;
        }
        return trans.size();
    }
};




/*
执行用时：4 ms, 在所有 C++ 提交中击败了58.65% 的用户
内存消耗：8.2 MB, 在所有 C++ 提交中击败了90.62% 的用户
通过测试用例：82 / 82
*/
class Solution {
public:
    unordered_set<string> trans;
    int uniqueMorseRepresentations(vector<string>& words) {
        string morse[26] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
                            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                            "...","-","..-","...-",".--","-..-","-.--","--.."};
        for (auto w: words) {
            string t = "";
            for (auto ch: w) {
                t += morse[ch - 'a'];
            }
            trans.insert(t);
        }
        return trans.size();
    }
};

/*
执行用时：4 ms, 在所有 C++ 提交中击败了58.65% 的用户
内存消耗：8.5 MB, 在所有 C++ 提交中击败了12.74% 的用户
通过测试用例：82 / 82
*/
class Solution {
public:
    unordered_set<string> trans;
    int uniqueMorseRepresentations(vector<string>& words) {
        string morse[26] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
                            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                            "...","-","..-","...-",".--","-..-","-.--","--.."};
        for (auto w: words) {
            string t = "";
            for (auto ch: w) {
                t += morse[ch - 'a'];
            }
            trans.emplace(t);
        }
        return trans.size();
    }
};



/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：8.4 MB, 在所有 C++ 提交中击败了20.43% 的用户
通过测试用例：82 / 82
*/
class Solution {
public:
    unordered_set<string> trans;
    vector<string> morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
                            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                            "...","-","..-","...-",".--","-..-","-.--","--.."};
    int uniqueMorseRepresentations(vector<string>& words) {
        
        for (auto w: words) {
            string t = "";
            for (auto ch: w) {
                t += morse[ch - 'a'];
            }
            trans.emplace(t);
        }
        return trans.size();
    }
};


/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：8.2 MB, 在所有 C++ 提交中击败了67.55% 的用户
通过测试用例：82 / 82
*/
class Solution {
public:
    unordered_set<string> trans;
    string morse[26] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
                            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                            "...","-","..-","...-",".--","-..-","-.--","--.."};
    int uniqueMorseRepresentations(vector<string>& words) {
        
        for (auto w: words) {
            string t = "";
            for (auto ch: w) {
                t += morse[ch - 'a'];
            }
            trans.emplace(t);
        }
        return trans.size();
    }
};

/*
执行用时：4 ms, 在所有 C++ 提交中击败了58.65% 的用户
内存消耗：8.3 MB, 在所有 C++ 提交中击败了56.73% 的用户
通过测试用例：82 / 82
*/
class Solution {
public:
    //unordered_set<string> trans;
    set<string> trans;
    string morse[26] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
                            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                            "...","-","..-","...-",".--","-..-","-.--","--.."};
    int uniqueMorseRepresentations(vector<string>& words) {
        
        for (auto w: words) {
            string t = "";
            for (auto ch: w) {
                t += morse[ch - 'a'];
            }
            trans.insert(t);
        }
        return trans.size();
    }
};


/*
执行用时：4 ms, 在所有 C++ 提交中击败了58.65% 的用户
内存消耗：8.2 MB, 在所有 C++ 提交中击败了70.91% 的用户
通过测试用例：82 / 82
*/
class Solution {
public:
    // set<string> trans;
    unordered_set<string> trans;
    vector<string> morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
                        ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                        "...","-","..-","...-",".--","-..-","-.--","--.."};      
    int uniqueMorseRepresentations(vector<string>& words) {
        for (int i = 0; i < words.size(); ++i) { 
            int len = words[i].size();
            for (int j = 0; j < len; j++) {
                words[i] += morse[words[i][j] - 'a'];
            }
            words[i].erase(0, len);
            trans.insert(words[i]);
        }
        return trans.size();
    }
};





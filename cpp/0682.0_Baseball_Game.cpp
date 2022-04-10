/*
Runtime: 7 ms, faster than 43.28% of C++ online submissions for Baseball Game.
Memory Usage: 8.4 MB, less than 28.60% of C++ online submissions for Baseball Game.
*/
class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> rounds;
        for (string op: ops) {
            if (op[0] == '+') {
                rounds.push_back(rounds[rounds.size() - 1] + rounds[rounds.size() - 2]);
            } else if (op[0] == 'D') {
                rounds.push_back(2 * rounds[rounds.size() - 1]);
            } else if (op[0] == 'C') {
                rounds.pop_back();
            } else {
                rounds.push_back(stoi(op));
            }
        }
        return accumulate(rounds.begin(), rounds.end(), 0);
    }
};


/*
Runtime: 8 ms, faster than 30.74% of C++ online submissions for Baseball Game.
Memory Usage: 8.3 MB, less than 95.60% of C++ online submissions for Baseball Game.
*/
class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> rounds;
        for (string op: ops) {
            if (op == "+") {
                rounds.push_back(rounds[rounds.size() - 1] + rounds[rounds.size() - 2]);
            } else if (op == "D") {
                rounds.push_back(2 * rounds[rounds.size() - 1]);
            } else if (op == "C") {
                rounds.pop_back();
            } else {
                rounds.push_back(stoi(op));
            }
        }
        return accumulate(rounds.begin(), rounds.end(), 0);
    }
};


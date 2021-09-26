/*
ref:
https://leetcode-cn.com/problems/transform-to-chessboard/solution/782-cchao-97de-shu-xue-fen-xi-jie-fa-by-tc8o8/

You are here!
Your runtime beats 58.93 % of cpp submissions.
You are here!
Your memory usage beats 55.36 % of cpp submissions.
*/

class Solution {
private:
    int n;
    int mask;
    
    int CntOneBit(int num) {
        int cnt = 0;
        while (num > 0) {
            if ((num & 1) == 1) {
                ++cnt;
            }
            num >>= 1;
        }
        return cnt;
    }
    
    int CalculateSteps(unordered_map<int, int>& code2num) {
        int codes[2];
        int nums[2];
        int cnt = 0;
        for (auto iter = code2num.begin(); iter != code2num.end(); ++iter) {
            codes[cnt] = iter->first;
            nums[cnt] = iter->second;
            ++cnt;
        }
        
        // use nums[0] codes[0]
        if (nums[0] < nums[1]) {
            swap(nums[0], nums[1]);
            swap(codes[0], codes[1]);
        }
        if (nums[0] != (n + 1) / 2 || nums[1] != n / 2) {
            return -1;
        }
        if ((codes[0] ^ codes[1]) != mask) {
            return -1;
        }
        // step
        if (n % 2 == 0) {
            return min(CntOneBit(codes[0] ^ 0x55555555 & mask), CntOneBit(codes[0] ^ 0xaaaaaaaa & mask)) >> 1;
        } else {
            int code = CntOneBit(codes[0]) > (n/2) ? codes[0] : codes[1];
            return CntOneBit((code ^ 0x55555555) & mask) / 2;
        }
    }
public:
    int movesToChessboard(vector<vector<int>>& board) {
        n = board.size();
        mask = (1 << n) - 1;
        unordered_map<int, int> code2num;
        // row
        for (int i = 0; i < n; ++i) {
            int curr = 0;
            for (int j = 0; j < n; ++j) {
                curr = (curr << 1) + board[i][j];
            }
            ++code2num[curr];
            if (code2num.size() > 2) {
                return -1;
            }
        }
        int stepsRow = CalculateSteps(code2num);
        if (stepsRow == -1) {
            return -1;
        }
        
        code2num.clear();
        // column
        for (int j = 0; j < n; ++j) {
            int curr = 0;
            for (int i = 0; i < n; ++i) {
                curr = (curr << 1) + board[i][j];
            }
            ++code2num[curr];
            if (code2num.size() > 2) {
                return -1;
            }
        }
        
        int stepsCol = CalculateSteps(code2num);
        if (stepsCol == -1) {
            return -1;
        }
        return stepsRow + stepsCol;
    }
};


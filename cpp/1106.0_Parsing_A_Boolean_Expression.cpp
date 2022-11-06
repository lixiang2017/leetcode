/*
stack
T: O(N)
S: O(N)

执行用时：12 ms, 在所有 C++ 提交中击败了33.78% 的用户
内存消耗：6.9 MB, 在所有 C++ 提交中击败了85.13% 的用户
通过测试用例：75 / 75
*/
class Solution {
public:
    bool parseBoolExpr(string expression) {
        int n = expression.size();
        stack<char> stk;
        for (char item : expression) {
            if (item != ',' && item != ')') {
                stk.push(item);
            } else if (item == ')') {
                int t = 0, f = 0;
                while (stk.top() != '(') {
                    char val = stk.top();
                    if (val == 't') t++;
                    else f++;
                    stk.pop();
                }
                stk.pop(); // pop '('
                char op = stk.top();
                stk.pop();
                if (op == '&') {
                    char ans = f > 0 ? 'f' : 't';
                    stk.push(ans);
                } else if (op == '|') {
                    char ans = t > 0 ? 't' : 'f';
                    stk.push(ans);
                } else { // '|'
                    char ans = t > 0 ? 'f' : 't';
                    stk.push(ans);
                }
            }
        }
        return stk.top() == 't';
    }
};


/*
recursion
T: O(N^2)
S: O(N)

执行用时：16 ms, 在所有 C++ 提交中击败了18.88% 的用户
内存消耗：17.1 MB, 在所有 C++ 提交中击败了9.04% 的用户
通过测试用例：75 / 75
*/
class Solution {
public:
    bool parseBoolExpr(string e) {
        if (e.size() == 1) {
            return e == "t" ? true : false;
        }
        if (e[0] == '!') {
            // 处理 !(...) 中 ... 的部分
            string subExp = e.substr(2, e.size() - 3);
            return !parseBoolExpr(subExp);
        }

        // 处理 !(...) 或 |(...) 中 ... 的部分
        bool res = e[0] == '&' ? true : false;  // 初始值
        int cnt = 0;  // 记录未匹配 '(' 的数量
        int start = 2, i = 2;  // start 指向每一个子表达式的起始位置
        while (i < e.size()) {
            if (e[i] == '(') {
                cnt++;
            }
            if (e[i] == ')') {
                cnt--;
            }
            /* 以 ',' 分割截取字符串并进行递归。cnt == 0 保证截取的表达式是完整的
            */
            if ((e[i] == ',' && cnt == 0) || i == e.size() - 1) {
                string subExp = e.substr(start, i - start);
                if (e[0] == '&') {
                    res &= parseBoolExpr(subExp);
                } else {
                    res |= parseBoolExpr(subExp);
                }
                start = i + 1;
            }
            i++;
        }
        return res;
    }
};



/*
recursive
每次只能从A的最上面转到到C，也即是 *A.rbegin() 或者 A.back()。
A[0] 代表是的最下面的，也就是最大的，是不对的。

执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：7.2 MB, 在所有 C++ 提交中击败了5.08% 的用户
通过测试用例：14 / 14
*/
class Solution {
public:
    void hanota(vector<int>& A, vector<int>& B, vector<int>& C) {
        // cout << "rbegin: " << *A.rbegin() << endl;
        // cout << "begin: " << *A.begin() << endl;
        // cout << "idx0: " << A[0] << endl;
        move(A.size(), A, B, C);
    }

    void move(int n, vector<int>& A, vector<int>& B, vector<int>& C) {
        if (n == 1) {
            // int x = A[0];  // wrong
            int x = *A.rbegin();
            A.pop_back();
            C.push_back(x);
            return;
        }
        move(n - 1, A, C, B);
        //int x = A[0];
        int x = *A.rbegin();
        A.pop_back();
        C.push_back(x);
        move(n - 1, B, A, C);
    }
};



/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：6.6 MB, 在所有 C++ 提交中击败了40.14% 的用户
通过测试用例：14 / 14
*/
class Solution {
public:
    void hanota(vector<int>& A, vector<int>& B, vector<int>& C) {
        move(A.size(), A, B, C);
    }

    void move(int n, vector<int>& A, vector<int>& B, vector<int>& C) {
        if (n == 1) {
            C.push_back(A.back());
            A.pop_back();
            return;
        }
        move(n - 1, A, C, B);
        C.push_back(A.back());
        A.pop_back();
        move(n - 1, B, A, C);
    }
};


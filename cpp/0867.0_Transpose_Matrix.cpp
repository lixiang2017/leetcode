/*
Time: O(M * N)
Space: O(M * N)

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 C++ 提交中击败了69.12%的用户
内存消耗：10.2 MB, 在所有 C++ 提交中击败了18.38%的用户
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int M = matrix.size(), N = matrix[0].size();
        vector<vector<int>> trans(N, vector<int>(M));
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                trans[j][i] = matrix[i][j];
            }
        }

        return trans;
    }
};


int main(int argc, char const *argv[])
{
	int one_matrix[3][3] = {{1, 2, 3},
							{4, 5, 6},
							{7, 8, 9}};
	vector<vector<int>> matrix(3, vector<int>(3));
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			matrix[i][j] = one_matrix[i][j];
		}
	}
	cout << "origin matrix:"  << endl;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			cout << matrix[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;

	Solution sol;
	vector<vector<int>> trans(3, vector<int>(3));
	trans = sol.transpose(matrix);
	cout << "transposed:"  << endl;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			cout << trans[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}


/*
g++ 0867.0_Transpose_Matrix.cpp
./a.out

origin matrix:
1 2 3 
4 5 6 
7 8 9 

transposed:
1 4 7 
2 5 8 
3 6 9
*/
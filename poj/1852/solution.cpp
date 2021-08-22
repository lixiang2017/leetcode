/*
Time Limit Exceeded


Sample Input

2
10 3
2 6 7
214 7
11 12 7 13 176 23 191

Sample Output

4 8
38 207

Source
Waterloo local 2004.09.19
*/

#include <iostream>
#include <algorithm>

using namespace std;

int solve(int L, int n, int* x) {
    int minT = 0;
    for (int i = 0; i < n; i++) {
        minT = max(minT, min(x[i], L - x[i]));
    }

    int maxT = 0;
    for (int i = 0; i < n; i++) {
        maxT = max(maxT, max(x[i], L - x[i]));
    }
    
    cout << minT << ' ' << maxT << endl;
    return 0;
}


int solve2(int L, int n, int* x) {
    int minT = 0;
    int maxT = 0;
    for (int i = 0; i < n; i++) {
        minT = max(minT, min(x[i], L - x[i]));
        maxT = max(maxT, max(x[i], L - x[i]));
    }

    cout << minT << ' ' << maxT << endl;
    return 0;
}

int main(void) {
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; i++) {
        int L, n;
        cin >> L >> n;
        int x[n];
        for (int j = 0; j < n; j++) {
            cin >> x[j];
        }
        solve2(L, n, x);
    }

    return 0;
}

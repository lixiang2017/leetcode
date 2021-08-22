/*
Problem: 1852       User: lixiang2021
Memory: 328K        Time: 125MS
Language: G++       Result: Accepted
*/


#include <cstdio>
#include <algorithm>

using namespace std;

int n, m, num;

int main() {
    int t = 0;
    scanf("%d", &t);
    while (t--) {
        int minx = -1, maxx = -1;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < m; i++) {
            scanf("%d", &num);
            minx = max(minx, min(num, n - num));
            maxx = max(maxx, max(num, n - num));
        }
        printf("%d %d\n", minx, maxx);
    }

    return 0;
}

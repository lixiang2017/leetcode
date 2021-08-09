/*
执行用时：768 ms, 在所有 C++ 提交中击败了14.75% 的用户
内存消耗：132.6 MB, 在所有 C++ 提交中击败了5.12% 的用户
*/

#include <unordered_set>
#include <queue>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        unordered_set<long> seen;
        priority_queue<long, vector<long>, greater<long> > h;
        seen.insert(1);
        h.push(1);
        int ugly = 0;
        for (int i = 0; i < n; i++) {
            long curr = h.top();
            h.pop();
            ugly = (int) curr;
            for (int prime: primes) {
                long next = curr * prime;
                if (seen.insert(next).second) {
                    h.push(next);
                }
            }
        }
        return ugly;
    }
};


int main()
{
    // case 1
    int ugly = 0;
    int n = 12;
    vector<int> primes {2, 7, 13, 19};
    ugly = Solution().nthSuperUglyNumber(n, primes);
    cout << "ugly = " << ugly << endl;

    // case 2
    n = 1;
    primes = {2, 3, 5};
    ugly = Solution().nthSuperUglyNumber(n, primes);
    cout << "ugly = " << ugly << endl;    

    cout << "done." << endl;
    return 0;
}


/*
# input
12
[2,7,13,19]
1
[2,3,5]

# output
32
1
*/



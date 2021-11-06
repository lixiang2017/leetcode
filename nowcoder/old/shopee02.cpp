// AC

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool judge(const int& stepLen, const vector<int>& num, int steps) {
    int tempSum = 0, cur = 0, i = 0, len = num.size();
    for (i = 0; i < len; ++i) {
        tempSum += num[i];
        if (tempSum > stepLen) {
            cur++;
            tempSum = num[i];
        }
        if (cur >= steps)
            break;
    }
    return i == len;
}
int main() {
    int n, m;
    cin >> n >> m;
    if (n <= 0)
        return 0;
    vector<int> num;
    int maxNum = 0, sumNum = 0, temp;
    for (int i = 0; i < n; ++i) {
        cin >> temp;
        num.push_back(temp);
        maxNum = max(maxNum, temp);
        sumNum += temp;
    }
    int left = maxNum, right = sumNum, ans = right, mid;
    while (left <= right) {
        mid = (left + right) / 2;
        if (judge(mid, num, m)) {
            right = mid - 1;
            ans = min(ans, mid);
        }
        else
            left = mid + 1;
    }
    cout << mid << endl;  //cout<<ans<<endl通过率只有50%
    return 0;
}
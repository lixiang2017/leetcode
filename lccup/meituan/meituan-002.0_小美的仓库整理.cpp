/*
set + map

ref:
https://leetcode-cn.com/problems/TJZLyC/solution/zhe-bu-bao-li-yi-bo-ma-qian-zhui-he-ying-vh9h/

执行用时：48 ms, 在所有 C++ 提交中击败了75.38% 的用户
内存消耗：5.5 MB, 在所有 C++ 提交中击败了41.48% 的用户
通过测试用例：10 / 10
*/
/*
输入：
5
3 2 4 4 5 
4 3 5 2 1
输出：
     9
     5
     5
     3
     0
解释：
原本的状态是 {{3,2,4,4,5}} ，取出 4 号货物后，得到 {{3,2,4},{5}} ，第一堆货物的和是 9 ，然后取出 3 号货物得到 {{3,2}{5}} ，此时第一堆和第二堆的和都是 5 ，以此类推。
*/

#include <cstdio>
#include <cstring>
#include <map>
#include <set>

int presum[50050];
// 区间和 -> 个数
std::map<int, int> seg_sum;
// 区间的边界，所有边界
std::set<int> bound;

int main() {
    int n;
    scanf("%d", &n);

    int w; // weight
    memset(presum, 0, sizeof(presum));
    for (int i = 0; i < n; i++) {
        scanf("%d", &w);
        presum[i + 1] = presum[i] + w;
    }

    int pos;  // taken position
    bound.insert(0);      // leftmost
    bound.insert(n + 1);  // rightmost
    for (int i = 0; i < n; i++) {
        scanf("%d", &pos);
        auto idx = bound.lower_bound(pos);
        // 由于 set 的迭代器只能自减，所以先给 right 赋值
        int right = *idx, left = *(--idx);
        int seg = presum[right - 1] - presum[left];
        if (seg_sum.find(seg) != seg_sum.end()) {
            if (seg_sum[seg] == 1) {
                seg_sum.erase(seg);
            } else {
                seg_sum[seg] --;
            }
        }
        int left_sum = presum[pos - 1] - presum[left];
        int right_sum = presum[right - 1] - presum[pos];
        bound.insert(pos);
        seg_sum[left_sum]++;
        seg_sum[right_sum]++;
        printf("%d\n", seg_sum.rbegin()->first);
    }

    return 0;
}


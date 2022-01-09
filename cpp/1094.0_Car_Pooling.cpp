/*
执行用时：12 ms, 在所有 C++ 提交中击败了62.96% 的用户
内存消耗：9.9 MB, 在所有 C++ 提交中击败了52.09% 的用户
通过测试用例：58 / 58
*/
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector<int> road(1001, 0);
        for(auto &t: trips) {
            road[t[1]] += t[0];
            road[t[2]] -= t[0];
        }
        int passengers = 0;
        for (auto r: road) {
            passengers += r;
            if (passengers > capacity) return false;
        }
        return true;
    }
};


/*
std::map is a sorted associative container that contains key-value pairs with unique keys.
Keys are sorted by using the comparison function Compare.
Search, removal, and insertion operations have logarithmic complexity.
Maps are usually implemented as red-black trees.

执行用时：8 ms, 在所有 C++ 提交中击败了93.40% 的用户
内存消耗：10.1 MB, 在所有 C++ 提交中击败了33.58% 的用户
通过测试用例：58 / 58
*/
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        map<int, int> m;
        for(auto &t: trips) {
            m[t[1]] += t[0];
            m[t[2]] -= t[0];
        }
        int passengers = 0;
        for (auto mm: m) {
            passengers += mm.second;
            if (passengers > capacity) return false;
        }
        return true;
    }
};


/*
sort + map

执行用时：16 ms, 在所有 C++ 提交中击败了25.93% 的用户
内存消耗：10 MB, 在所有 C++ 提交中击败了41.87% 的用户
通过测试用例：58 / 58
*/
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        sort(trips.begin(), trips.end(),
            [&] (const vector<int> &t1, const vector<int> &t2) {
                return t1[1] < t2[1];
            }
        );

        map<int, int> m; // {end => passengers};
        int passengers = 0;
        for (auto t: trips) {
            for (auto it = m.begin(); it != m.end();) {
                if (it->first <= t[1]) {
                    passengers -= it->second;
                    m.erase(it++);
                } else {
                    break;
                }
            }
            // new passengers get on
            passengers += t[0];
            if (passengers > capacity) {
                return false;
            }
            m[t[2]] += t[0];
        }
        return true;
    }
};

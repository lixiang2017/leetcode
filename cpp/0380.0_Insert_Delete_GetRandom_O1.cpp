/*
vector + unordered_map

执行用时：192 ms, 在所有 C++ 提交中击败了66.22% 的用户
内存消耗：94.7 MB, 在所有 C++ 提交中击败了69.15% 的用户
通过测试用例：19 / 19
*/
class RandomizedSet {
private:
    // values
    vector<int> v;
    // val -> index in array/v
    unordered_map<int, int> m;

public:
    RandomizedSet() {
    }
    
    bool insert(int val) {
        if (m.count(val)) return false;
        v.push_back(val);
        m[val] = v.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        if (!m.count(val)) return false;
        int to_delete_idx = m[val];
        int last_one = v.back();
        m[last_one] = to_delete_idx;
        v[to_delete_idx] = last_one;
        v.pop_back();
        m.erase(val);
        return true;
    }
    
    int getRandom() {
        return v[rand() % v.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */

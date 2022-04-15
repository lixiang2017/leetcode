/*
List + Map + Random

执行用时：20 ms, 在所有 Java 提交中击败了98.92% 的用户
内存消耗：90.2 MB, 在所有 Java 提交中击败了35.13% 的用户
通过测试用例：19 / 19
*/
class RandomizedSet {
    List<Integer> l = new ArrayList();
    Map<Integer, Integer> m = new HashMap<>();
    Random r = new Random();

    public RandomizedSet() {
    }
    
    public boolean insert(int val) {
        if (m.containsKey(val)) return false;
        l.add(val);
        m.put(val, l.size() - 1);
        return true;
    }
    
    public boolean remove(int val) {
        if (!m.containsKey(val)) return false;
        int to_delete_idx = m.get(val);
        int last_one = l.get(l.size() - 1);
        l.set(to_delete_idx, last_one);
        m.put(last_one, to_delete_idx);
        l.remove(l.size() - 1);
        m.remove(val);
        return true;
    }
    
    public int getRandom() {
        return l.get(r.nextInt(l.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */

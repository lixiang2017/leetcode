/*
HashMap

执行用时：2 ms, 在所有 Java 提交中击败了94.53% 的用户
内存消耗：38 MB, 在所有 Java 提交中击败了75.00% 的用户
通过测试用例：103 / 103
*/

class Solution {
    public String destCity(List<List<String>> paths) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (List<String> p: paths)
            map.put(p.get(0), 1);
        for (List<String> p: paths)
            if (map.get(p.get(1)) == null)
                return p.get(1);
        return null;  // need
    }
}

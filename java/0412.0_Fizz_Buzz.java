/*
执行用时：2 ms, 在所有 Java 提交中击败了49.78% 的用户
内存消耗：39.6 MB, 在所有 Java 提交中击败了56.25% 的用户
通过测试用例：8 / 8
*/

class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ans = new ArrayList<>();
        for (Integer i = 1; i <= n; i++) {
            if (i % 15 == 0) ans.add("FizzBuzz");
            else if (i % 3 == 0) ans.add("Fizz");
            else if (i % 5 == 0) ans.add("Buzz");
            else ans.add(i.toString());
        }
        return ans;
    }
}

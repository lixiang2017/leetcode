/*
执行用时：2 ms, 在所有 Java 提交中击败了20.33% 的用户
内存消耗：40.8 MB, 在所有 Java 提交中击败了40.67% 的用户
通过测试用例：99 / 99
*/

class Solution {
    public int minOperations(String[] logs) {
        Stack<String> stk = new Stack<String>();
        for (String op: logs) {
            if (op.equals("../")) {
                if (stk.size() != 0) {
                    stk.pop();
                }
            } else {
                if (!op.equals("./")) {
                    stk.push(op);
                }
            }
        }
        return stk.size();
    }
}

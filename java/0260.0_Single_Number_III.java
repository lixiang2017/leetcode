/*
bit manipulation

执行用时：1 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：38.6 MB, 在所有 Java 提交中击败了60.15% 的用户
通过测试用例：32 / 32
*/

class Solution {
    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int i = 0; i < nums.length; i++) {
            xor ^= nums[i];
        }
        int lowestOneBit = Integer.lowestOneBit(xor);
        int num1 = 0, num2 = 0;
        for (int i = 0; i < nums.length; i++) {
            if ((nums[i] & lowestOneBit) == 0){
                num1 ^= nums[i];
            } else {
                num2 ^= nums[i];
            }
        }
        return new int[]{num1, num2};
    }
}

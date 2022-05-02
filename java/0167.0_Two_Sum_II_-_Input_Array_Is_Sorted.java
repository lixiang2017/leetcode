/*
two pointers
T: O(N)
S: O(1)

执行用时：1 ms, 在所有 Java 提交中击败了92.70% 的用户
内存消耗：44.3 MB, 在所有 Java 提交中击败了24.58% 的用户
通过测试用例：21 / 21
*/
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] indices = new int[2];
        int i = 0, j = numbers.length - 1;
        while (i < j) {
            int s = numbers[i] + numbers[j];
            if (s == target) {
                indices[0] = i + 1;
                indices[1] = j + 1;
                return indices;
            } else if (s > target) {
                j--;
            } else {
                i++;
            }
        }
        return indices;
    }
}



/*
执行用时：1 ms, 在所有 Java 提交中击败了92.70% 的用户
内存消耗：44.5 MB, 在所有 Java 提交中击败了5.10% 的用户
通过测试用例：21 / 21
*/
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0, j = numbers.length - 1; i < j; ) {
            int sum = numbers[i] + numbers[j];
            if (sum == target) {
                return new int[] {i + 1, j + 1};
            } else if (sum > target) {
                j--;
            } else {
                i++;
            }
        }
        return null;
    }
}


/*
1ms 击败 100.00%使用 Java 的用户
42.41MB 击败 54.16%使用 Java 的用户
*/
class Solution {
    public boolean validMountainArray(int[] arr) {
        int start = 0, end = arr.length - 1;
        while (start < end && arr[start + 1] > arr[start]) {
            start++;
        }
        while (start < end && arr[end - 1] > arr[end]) {
            end--;
        }
        return start == end && start > 0 && end < arr.length - 1;
    }
}

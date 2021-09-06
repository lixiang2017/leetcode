/*
TreeMap + TreeSet

ref:
https://leetcode-cn.com/problems/TJZLyC/solution/zhe-bu-bao-li-yi-bo-ma-qian-zhui-he-ying-vh9h/

执行用时：268 ms, 在所有 Java 提交中击败了64.99% 的用户
内存消耗：50.8 MB, 在所有 Java 提交中击败了52.96% 的用户
通过测试用例：10 / 10
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {
    static TreeMap<Integer, Integer> seg_sum = new TreeMap<>();
    static TreeSet<Integer> bound = new TreeSet<>();
    static int[] presum = new int[50050];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");
        String[] query = br.readLine().split(" ");
        br.close();

        for (int i = 0; i < n; i++) {
            presum[i + 1] = presum[i] + Integer.parseInt(arr[i]);
        }

        bound.add(0);
        bound.add(n + 1);
        for (int i = 0; i < n; i++) {
            int pos = Integer.parseInt(query[i]);
            var left = bound.lower(pos);
            var right = bound.higher(pos);
            if (left == null || right == null) {
                continue;
            }
            int seg = presum[right - 1] - presum[left];
            var cnt = seg_sum.get(seg);
            if (cnt != null) {
                if (cnt == 1) {
                    seg_sum.remove(seg);
                } else {
                    seg_sum.put(seg, cnt - 1);
                }
            }
            int left_sum = presum[pos - 1] - presum[left];
            int right_sum = presum[right - 1] - presum[pos];
            bound.add(pos);
            seg_sum.put(left_sum, seg_sum.getOrDefault(left_sum, 0) + 1);
            seg_sum.put(right_sum, seg_sum.getOrDefault(right_sum, 0) + 1);
            bw.write(seg_sum.lastKey() + "\n");
        }
        bw.close();
    }
}

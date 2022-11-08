/*
Runtime: 31 ms, faster than 79.29% of C# online submissions for Maximum 69 Number.
Memory Usage: 25.8 MB, less than 27.81% of C# online submissions for Maximum 69 Number.
*/
public class Solution {
    public int Maximum69Number (int num) {
        foreach (var m in new List<int>{1000, 100, 10, 1}) {
            if (num / m % 10 == 6) {
                return num + m * 3;
            }
        }
        return num;
    }
}


/*
Runtime: 40 ms, faster than 54.44% of C# online submissions for Maximum 69 Number.
Memory Usage: 24.9 MB, less than 94.67% of C# online submissions for Maximum 69 Number.
*/
public class Solution {
    public int Maximum69Number (int num) {
        char[] s = num.ToString().ToCharArray();
        for (int i = 0; i < s.Length; ++i) {
            if (s[i] == '6') {
                s[i] = '9';
                return int.Parse(s);
            }
        }
        return num;
    }
}

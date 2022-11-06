/*
执行用时：68 ms, 在所有 C# 提交中击败了96.77% 的用户
内存消耗：36 MB, 在所有 C# 提交中击败了83.87% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public string Interpret(string command) {
        var ans = command.Replace("()", "o").Replace("(al)", "al");
        return ans;
    }
}


/*
执行用时：76 ms, 在所有 C# 提交中击败了54.84% 的用户
内存消耗：36.2 MB, 在所有 C# 提交中击败了45.16% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public string Interpret(string command) {
        return command.Replace("()", "o").Replace("(al)", "al");
    }
}


/*
执行用时：68 ms, 在所有 C# 提交中击败了96.77% 的用户
内存消耗：36.2 MB, 在所有 C# 提交中击败了41.94% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public string Interpret(string command) {
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < command.Length; ++i) {
            if ('G' == command[i]) {
                ans.Append('G');
            } else if ('(' == command[i]) {
                if (')' == command[i + 1]) {
                    ans.Append('o');
                } else {
                    ans.Append("al");
                }
            }
        }
        return ans.ToString();
    }
}


/*
执行用时：68 ms, 在所有 C# 提交中击败了96.77% 的用户
内存消耗：36.2 MB, 在所有 C# 提交中击败了22.58% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public string Interpret(string command) {
        string ans = "";
        for (int i = 0; i < command.Length; ++i) {
            if ('G' == command[i]) {
                ans += 'G';
            } else if ('(' == command[i]) {
                if (')' == command[i + 1]) {
                    ans += 'o';
                } else {
                    ans += "al";
                }
            }
        }
        return ans;
    }
}


/*
执行用时：76 ms, 在所有 C# 提交中击败了54.84% 的用户
内存消耗：36.2 MB, 在所有 C# 提交中击败了32.26% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public string Interpret(string command) {
        string ans = "";
        for (int i = 0; i < command.Length; ++i) {
            if ('G' == command[i]) {
                ans += "G";
            } else if ('(' == command[i]) {
                if (')' == command[i + 1]) {
                    ans += "o";
                } else {
                    ans += "al";
                }
            }
        }
        return ans;
    }
}



/*
执行用时：72 ms, 在所有 C# 提交中击败了80.65% 的用户
内存消耗：36.3 MB, 在所有 C# 提交中击败了19.35% 的用户
通过测试用例：105 / 105
*/
public class Solution {
    public string Interpret(string command) {
        List<(string oldStr, string newStr)> rep = new List<(string, string)>
        {
            ("()", "o"),
            ("(al)", "al"),
        };
        foreach (var item in rep) {
            command = command.Replace(item.oldStr, item.newStr);
        }
        return command;
    }
}

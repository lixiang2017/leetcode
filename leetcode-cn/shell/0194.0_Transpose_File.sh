
# 执行用时：8 ms, 在所有 Bash 提交中击败了72.00% 的用户
# 内存消耗：3.7 MB, 在所有 Bash 提交中击败了93.62% 的用户
# 通过测试用例：17 / 17

# Read from the file file.txt and print its transposed content to stdout.
awk '{
    # 这个大括号里的代码是对正文的处理
    # NF 表示列数，NR表示已读的行数
    # 注意for中的 i 从1开始，i前没有类型
    for (i = 1; i <= NF; i++) {   # 对每一列
        if (NR == 1) {    # 如果是第一行
            # 将第i列的值存入res[i], $i表示第i列的值，i为数组的下标，以列序号为下标
            # 数组不用定义可以直接使用
            res[i] = $i
        } else {
            # 不是第一行时，将该行对应 i 列的值拼接到res[i]
            res[i] = res[i] " " $i 
        }
    }
}

# BEGIN{} 文件扫描前要执行的操作；END{} 文件扫描后要执行的操作
END {
    # output
    for (i = 1; i <=NF; i++) {
        print res[i]
    }
}' file.txt 

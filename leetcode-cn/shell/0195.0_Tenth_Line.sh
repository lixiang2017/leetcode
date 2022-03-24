# 执行用时：0 ms, 在所有 Bash 提交中击败了100.00% 的用户
# 内存消耗：3.5 MB, 在所有 Bash 提交中击败了81.29% 的用户
# 通过测试用例：7 / 7

# Read from the file file.txt and output the tenth line to stdout.
tail -n +10 file.txt | head -1



# 执行用时：4 ms, 在所有 Bash 提交中击败了76.83% 的用户
# 内存消耗：3.6 MB, 在所有 Bash 提交中击败了44.93% 的用户
# 通过测试用例：7 / 7
# Read from the file file.txt and output the tenth line to stdout.
sed -n 10p file.txt



# 执行用时：4 ms, 在所有 Bash 提交中击败了76.83% 的用户
# 内存消耗：3.9 MB, 在所有 Bash 提交中击败了9.24% 的用户
# 通过测试用例：7 / 7
# Read from the file file.txt and output the tenth line to stdout.
## NR     ordinal number of the current record
awk 'NR == 10' file.txt



# 执行用时：56 ms, 在所有 Bash 提交中击败了5.82% 的用户
# 内存消耗：8.5 MB, 在所有 Bash 提交中击败了5.07% 的用户
# 通过测试用例：7 / 7
# Read from the file file.txt and output the tenth line to stdout.
python3 -c '
with open("file.txt") as f:
    try:
        print(f.readlines()[9].strip())  # strip是为了消除结尾\n
    except:
        pass  # 没有十行的情况
'


# 执行用时：56 ms, 在所有 Bash 提交中击败了5.82% 的用户
# 内存消耗：8.4 MB, 在所有 Bash 提交中击败了5.07% 的用户
# 通过测试用例：7 / 7
# Read from the file file.txt and output the tenth line to stdout.
python3 -c '
with open("file.txt") as f:
    for _ in range(9):
        f.readline()
    print(f.readline(), end = "")
'


# 执行用时：48 ms, 在所有 Bash 提交中击败了5.82% 的用户
# 内存消耗：8.6 MB, 在所有 Bash 提交中击败了5.07% 的用户
# 通过测试用例：7 / 7
# Read from the file file.txt and output the tenth line to stdout.
python3 -c "print(next((line for i, line in enumerate(open('file.txt', 'r', encoding='utf-8')) if i == 9), ''), end='')"




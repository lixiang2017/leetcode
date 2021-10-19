/*
执行用时：535 ms, 在所有 MySQL 提交中击败了39.36% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：21 / 21
*/

# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from 
(
    select num,
    lead(num, 1) over () as next1,
    lead(num, 2) over () as next2
    from logs 
) a where num = next1 and num = next2


# Every derived table must have its own alias

/*
输入：
{"headers": {"Logs": ["Id", "Num"]}, "rows": {"Logs": [[1, 3], [2, 3], [3, 3], [4, 3]]}}
输出：
{"headers": ["ConsecutiveNums"], "values": [[3], [3]]}
预期结果：
{"headers":["ConsecutiveNums"],"values":[[3]]}
*/



/*
执行用时：508 ms, 在所有 MySQL 提交中击败了82.78% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：21 / 21
*/
# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from 
(
    select num,
    lag(num, 1) over () as pre1,
    lag(num, 2) over () as pre2
    from logs 
) a where num = pre1 and num = pre2


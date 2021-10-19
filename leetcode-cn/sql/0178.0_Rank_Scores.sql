/*
执行用时：414 ms, 在所有 MySQL 提交中击败了36.15% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：10 / 10
*/
# Write your MySQL query statement below
select score as `Score`,
dense_rank() over (order by score desc) as `Rank`
from scores
order by score desc



/*
执行用时：268 ms, 在所有 MySQL 提交中击败了98.77% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：10 / 10
*/
# Write your MySQL query statement below
select score as `Score`,
dense_rank() over (order by score desc) as `Rank`
from scores

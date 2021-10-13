/*
执行用时：572 ms, 在所有 MySQL 提交中击败了9.46% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/

# Write your MySQL query statement below
select a.id from weather a
join weather b 
on a.temperature > b.temperature and datediff(a.recorddate, b.recorddate) = 1



/*
执行用时：457 ms, 在所有 MySQL 提交中击败了76.59% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select a.id from weather a, weather b 
where a.temperature > b.temperature and datediff(a.recorddate, b.recorddate) = 1

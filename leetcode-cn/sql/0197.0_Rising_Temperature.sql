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


/*
执行用时：477 ms, 在所有 MySQL 提交中击败了43.43% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select a.id from weather a cross join weather b 
on a.temperature > b.temperature and datediff(a.recorddate, b.recorddate) = 1


/*
14 / 14 个通过测试用例
状态：通过
执行用时: 499 ms
内存消耗: 0 B
提交时间：3 分钟前
*/
# Write your MySQL query statement below
select a.id from weather a cross join weather b 
where a.temperature > b.temperature and datediff(a.recorddate, b.recorddate) = 1


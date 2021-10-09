/*
执行用时：250 ms, 在所有 MySQL 提交中击败了27.57% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：4 / 4
*/
# Write your MySQL query statement below
select name, population, area from world
where area > 3 * 1000000 or population > 25 * 1000000


/*
执行用时：229 ms, 在所有 MySQL 提交中击败了46.25% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：4 / 4
*/
# Write your MySQL query statement below
select name, population, area from world
where area > 3 * power(10, 6) or population > 25 * power(10, 6)



/*
union有distinct 功能,union all是不筛选重复,会有两条重复记录

执行用时：225 ms, 在所有 MySQL 提交中击败了57.92% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：4 / 4
*/
# Write your MySQL query statement below
select name, population, area from world
where area > 3 * power(10, 6) 
union
select name, population, area from world
where population > 25 * power(10, 6)


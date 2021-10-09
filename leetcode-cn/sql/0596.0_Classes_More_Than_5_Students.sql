/*
Every derived table must have its own alias

执行用时：322 ms, 在所有 MySQL 提交中击败了19.29% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：9 / 9
*/
# Write your MySQL query statement below
select class from (
    select class, count(class) as cnt from 
    (
        select distinct * from courses
    ) b
    group by class
) a where cnt >= 5


/*
执行用时：274 ms, 在所有 MySQL 提交中击败了92.92% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：9 / 9
*/
# Write your MySQL query statement below
select class from 
(
    select distinct * from courses
) a group by class having count(class) >= 5


/*
student

执行用时：313 ms, 在所有 MySQL 提交中击败了24.99% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：9 / 9
*/
# Write your MySQL query statement below
select class from 
(
    select distinct * from courses
) a group by class having count(student) >= 5


/*
执行用时：324 ms, 在所有 MySQL 提交中击败了18.31% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：9 / 9
*/
# Write your MySQL query statement below
select class from courses
group by class having count(distinct student) >= 5


/*
执行用时：284 ms, 在所有 MySQL 提交中击败了63.98% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：9 / 9
*/
# Write your MySQL query statement below
select class from
(
    select class, count(class) as cnt from 
    (
        select class from courses group by student, class
    ) a group by class 
) b where cnt >= 5







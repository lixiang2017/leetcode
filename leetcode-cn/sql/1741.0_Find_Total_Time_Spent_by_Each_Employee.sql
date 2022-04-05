/*
执行用时：534 ms, 在所有 MySQL 提交中击败了80.54% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
# 27 + 145 = 173
select 
    event_day as `day`,
    emp_id,
    sum(out_time) - sum(in_time) as `total_time`
from employees
group by event_day, emp_id


/*
执行用时：550 ms, 在所有 MySQL 提交中击败了57.61% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select 
    event_day as `day`,
    emp_id,
    sum(out_time - in_time) as `total_time`
from employees
group by event_day, emp_id


/*
执行用时：545 ms, 在所有 MySQL 提交中击败了65.32% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select 
    event_day as `day`,
    emp_id,
    sum(out_time - in_time) as `total_time`
from employees
group by 1, 2

/*
执行用时：918 ms, 在所有 MySQL 提交中击败了56.92% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：19 / 19
*/
# Write your MySQL query statement below
select d.name as department,
a.name as employee,
salary
from 
(
    select *,
    dense_rank() over (partition by departmentid order by salary desc) as r
    from employee 
) a 
join department d on a.departmentid = d.id
where a.r <= 3


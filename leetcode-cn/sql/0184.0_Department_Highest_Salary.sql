/*
执行用时：667 ms, 在所有 MySQL 提交中击败了93.05% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select d.name as Department, b.name as Employee, Salary
from 
(   
    select * from 
    (
        select 
        name, 
        salary,
        departmentid,
        rank() over (partition by departmentid order by salary desc) as r
        from Employee
    ) a where r = 1
) b join 
department d on b.departmentid = d.id

/*
执行用时：380 ms, 在所有 MySQL 提交中击败了72.04% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select e1.Name as Employee
from Employee e1, Employee e2
where e1.ManagerId = e2.Id and e1.Salary > e2.Salary



/*
join 

执行用时：403 ms, 在所有 MySQL 提交中击败了39.90% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select e1.Name as Employee
from Employee e1 
join Employee e2
on e1.ManagerId = e2.Id and e1.Salary > e2.Salary



/*
left join

执行用时：374 ms, 在所有 MySQL 提交中击败了85.03% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select e1.Name as Employee
from Employee e1 
left join Employee e2
on e1.ManagerId = e2.Id 
where e1.Salary > e2.Salary 


/*
inner join

执行用时：388 ms, 在所有 MySQL 提交中击败了57.27% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select e1.Name as Employee
from Employee e1 
inner join Employee e2
on e1.ManagerId = e2.Id and e1.Salary > e2.Salary


/*
right join

执行用时：519 ms, 在所有 MySQL 提交中击败了12.73% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select e1.Name as Employee
from Employee e1 
right join Employee e2
on e1.ManagerId = e2.Id 
where e1.Salary > e2.Salary 




/*
执行用时：1226 ms, 在所有 MySQL 提交中击败了5.02% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
# Write your MySQL query statement below
select e.Name as Employee
from Employee e
where salary > (select salary from Employee where id = e.ManagerId)



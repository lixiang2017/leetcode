# Write your MySQL query statement below
select e1.Name as Employee from Employee e1, Employee e2
where e1.ManagerId = e2.id and e1.Salary > e2.Salary

# Success
# Details 
# Runtime: 621 ms, faster than 20.01% of MySQL online submissions for Employees Earning More Than Their Managers.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.

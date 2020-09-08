# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary from Employee where Salary <
    (select max(Salary) from Employee)
# Success
# Details 
# Runtime: 202 ms, faster than 90.37% of MySQL online submissions for Second Highest Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
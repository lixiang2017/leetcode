/* MS SQL Server*/
/* Write your T-SQL query statement below */
with a as(
    select id,salary,rank() over (order by salary desc) as ran from employee
)
select 
max(salary) as SecondHighestSalary from a where a.ran=2;
/* max returns null if value not found*/

/*
Success
Details 
Runtime: 1718 ms, faster than 5.88% of MS SQL Server online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MS SQL Server online submissions for Second Highest Salary.
*/
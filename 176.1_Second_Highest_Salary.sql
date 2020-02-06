# Write your MySQL query statement below
SELECT distinct(Salary) as SecondHighestSalary FROM Employee 
UNION 
SELECT NULL
ORDER BY SecondHighestSalary DESC LIMIT 1, 1;
# Success
# Details 
# Runtime: 313 ms, faster than 64.10% of MySQL online submissions for Second Highest Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.
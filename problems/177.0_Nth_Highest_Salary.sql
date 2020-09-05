CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from
      (
          select Salary, dense_rank() over (order by Salary desc) as r from Employee
      ) as t where r = N
  );
END

Success
Details
Runtime: 718 ms, faster than 24.98% of MySQL online submissions for Nth Highest Salary.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Nth Highest Salary.


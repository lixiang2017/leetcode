/*
执行用时：363 ms, 在所有 MySQL 提交中击败了72.28% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select ifnull((
          salary
      ), null) from (
          select distinct salary,
          dense_rank() over (order by salary desc) as salary_rank
          from employee
      ) a where salary_rank = N
  );
END



/*
执行用时：375 ms, 在所有 MySQL 提交中击败了48.95% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from employee order by salary desc limit N, 1
  );
END



/*
执行用时：440 ms, 在所有 MySQL 提交中击败了11.99% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N - 1;
  if n < 0 then 
  return null;
  else 
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from employee order by salary desc limit N, 1
  );
  end if;
END



/*
执行用时：390 ms, 在所有 MySQL 提交中击败了31.14% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
*/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary
      from 
      (
          select salary,
          dense_rank() over (order by salary desc) as salary_rank
          from employee
      ) a where salary_rank = N
  );
END

/*
执行用时：220 ms, 在所有 MySQL 提交中击败了37.40% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：7 / 7
*/

# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from 
(
    select *, 
    dense_rank() over (order by salary desc) as d_rank
    from employee
) a where d_rank = 2



/*
执行用时：218 ms, 在所有 MySQL 提交中击败了40.60% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：7 / 7
*/
# Write your MySQL query statement below
select if(count(*) != 0, salary, null) as SecondHighestSalary from 
(select *,
    dense_rank() over (order by salary desc) as ranking
    from employee 
) a where ranking = 2


/*
执行用时：248 ms, 在所有 MySQL 提交中击败了26.05% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select if(count(1) != 0, salary, null)  secondhighestsalary from (
    select salary,
    dense_rank() over (order by salary desc) as d_rank 
    from employee 
) a where d_rank = 2


/*
执行用时：126 ms, 在所有 MySQL 提交中击败了97.40% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select if(count(1) = 0, null, salary)  secondhighestsalary from (
    select salary,
    dense_rank() over (order by salary desc) as d_rank 
    from employee 
) a where d_rank = 2





/*
执行用时：218 ms, 在所有 MySQL 提交中击败了40.60% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：7 / 7
*/
# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from employee
where salary <> (select max(salary) from employee)


/*
执行用时：273 ms, 在所有 MySQL 提交中击败了6.00% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：7 / 7
*/
# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from employee
where salary < (select max(salary) from employee)


/*
执行用时：207 ms, 在所有 MySQL 提交中击败了71.64% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：7 / 7
*/
# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from employee
where salary not in (select max(salary) from employee)


/*
执行用时：253 ms, 在所有 MySQL 提交中击败了10.99% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：7 / 7
*/
# Write your MySQL query statement below
select max(e1.salary) as SecondHighestSalary
from employee e1, employee e2
where e1.salary < e2.salary


/*
执行用时：199 ms, 在所有 MySQL 提交中击败了96.33% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：7 / 7
*/
# Write your MySQL query statement below
select IFNULL((
    select salary from 
    (
        select salary,
        dense_rank() over (order by salary desc) as salaryrank 
        from Employee
    ) as t
    where salaryrank = 2 limit 1
), null) as SecondHighestSalary 


/*
执行用时：208 ms, 在所有 MySQL 提交中击败了67.00% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：7 / 7
*/
# Write your MySQL query statement below
select ifnull((
    select distinct salary from 
    (
        select salary,
        dense_rank() over (order by salary desc) as salaryrank 
        from Employee
    ) as t
    where salaryrank = 2
), null) as SecondHighestSalary 


/*
执行用时：208 ms, 在所有 MySQL 提交中击败了67.00% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：7 / 7
*/
# Write your MySQL query statement below
select ifnull((
    select distinct salary
    from Employee
    order by salary desc
    limit 1, 1
), null) as SecondHighestSalary 




/*
执行用时：129 ms, 在所有 MySQL 提交中击败了96.91% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select ifnull(
(select distinct salary from employee order by salary desc limit 1, 1),
null
) as secondhighestsalary


/*
执行用时：228 ms, 在所有 MySQL 提交中击败了51.19% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select 
(select distinct salary from employee order by salary desc limit 1, 1) 
as secondhighestsalary


/*
执行用时：126 ms, 在所有 MySQL 提交中击败了97.40% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select 
(select distinct salary from employee order by salary desc limit 1 offset 1) 
as secondhighestsalary



/*
执行用时：130 ms, 在所有 MySQL 提交中击败了96.77% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select max(salary) secondhighestsalary from employee 
where salary < (select max(salary) from employee)


/*
执行用时：130 ms, 在所有 MySQL 提交中击败了96.77% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select min(salary) secondhighestsalary from (
    select salary,
    dense_rank() over (order by salary desc) as d_rank 
    from employee 
) a where d_rank = 2



/*
执行用时：126 ms, 在所有 MySQL 提交中击败了97.40% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
select avg(salary) secondhighestsalary from (
    select salary,
    dense_rank() over (order by salary desc) as d_rank 
    from employee 
) a where d_rank = 2






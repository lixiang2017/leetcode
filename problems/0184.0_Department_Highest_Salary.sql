# Write your MySQL query statement below
select d.name as department, e1.name as employee, e1.salary
from employee e1
join department d on e1.departmentid = d.id
where salary in 
(
    select max(salary) from employee e2
    where e1.departmentid = e2.departmentid
)

# Success
# Details 
# Runtime: 918 ms, faster than 48.80% of MySQL online submissions for Department Highest Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Department Highest Salary.


# Write your MySQL query statement below
# not use join
select d.name as department, e.name as employee, e.salary
from employee e, department d
where e.departmentid = d.id and 
    e.salary = (select max(salary) from employee e2 where e2.departmentid = d.id)


# Success
# Details 
# Runtime: 961 ms, faster than 45.93% of MySQL online submissions for Department Highest Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Department Highest Salary.


# Write your MySQL query statement below
# not use max 
select d.name as department, e.name as employee, e.salary
from employee e, department d
where e.departmentid = d.id and 
    e.salary >= all (select salary from employee e2 where e2.departmentid = d.id)

# Success
# Details 
# Runtime: 764 ms, faster than 60.27% of MySQL online submissions for Department Highest Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Department Highest Salary.


# Write your MySQL query statement below
# use group by
select d.name as department, e.name as employee, e.salary
from employee e, department d
where e.departmentid = d.id and
    (departmentid, salary) in
    (select departmentid, max(salary) from employee group by departmentid)

# Success
# Details 
# Runtime: 604 ms, faster than 88.10% of MySQL online submissions for Department Highest Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Department Highest Salary.


# Write your MySQL query statement below
# use join & group by
select d.name as department, e.name as employee, e.salary
from employee e join department d
on e.departmentid = d.id where
    (departmentid, salary) in
    (select departmentid, max(salary) from employee group by departmentid)

# Success
# Details 
# Runtime: 543 ms, faster than 97.15% of MySQL online submissions for Department Highest Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Department Highest Salary.












/*
执行用时：602 ms, 在所有 MySQL 提交中击败了53.81% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select employee_id, 
case when employee_id % 2 = 1 and substr(name, 1, 1) != 'M' then salary 
     else 0
end 
as bonus
from employees
order by employee_id 



# Write your MySQL query statement below
select employee_id, 
case when employee_id % 2 = 1 and substring(name, 1, 1) != 'M' then salary 
     else 0
end 
as bonus
from employees
order by employee_id 




/*
执行用时：578 ms, 在所有 MySQL 提交中击败了76.48% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select employee_id, 
    case when mod(employee_id, 2) != 0 and name not like 'M%' then salary 
        else 0 
    end 
    as bonus
from employees
order by employee_id 


/*
执行用时：615 ms, 在所有 MySQL 提交中击败了43.32% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select employee_id, 
    if (employee_id % 2 = 1 and left(name, 1) != 'M', salary, 0)
    as bonus
from employees
order by employee_id 


/*
执行用时：589 ms, 在所有 MySQL 提交中击败了66.13% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select employee_id, 
    if (employee_id % 2 = 1 && left(name, 1) != 'M', salary, 0)
    as bonus
from employees
order by employee_id 


/*
执行用时：587 ms, 在所有 MySQL 提交中击败了68.04% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select employee_id, 
    case when employee_id % 2 = 0 then 0
        when name like 'M%' then 0
        else salary
    end
    as bonus
from employees
order by employee_id 




'''
执行用时：624 ms, 在所有 MySQL 提交中击败了33.84% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select employee_id from employees 
where employee_id not in (select employee_id from salaries)
union 
select employee_id from salaries
where employee_id not in (select employee_id from employees)
order by employee_id


'''
执行用时：1644 ms, 在所有 MySQL 提交中击败了5.02% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：16 / 16
'''
# Write your MySQL query statement below
select 
    name,
    sum(amount) as balance 
from users as u, transactions as t
where u.account = t.account 
group by t.account 
having balance > 10000


'''
group by u.account 

执行用时：782 ms, 在所有 MySQL 提交中击败了50.86% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：16 / 16
'''
# Write your MySQL query statement below
select 
    name,
    sum(amount) as balance 
from users as u, transactions as t
where u.account = t.account 
group by u.account 
having balance > 10000

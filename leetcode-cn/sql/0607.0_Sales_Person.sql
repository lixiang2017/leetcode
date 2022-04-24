'''
执行用时：1404 ms, 在所有 MySQL 提交中击败了63.40% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：20 / 20
'''
# Write your MySQL query statement below
select name 
from salesperson where sales_id not in 
(
    select s.sales_id
    from company c 
    join orders o on c.com_id = o.com_id
    join salesperson s on o.sales_id = s.sales_id 
    where c.name = 'red'
)


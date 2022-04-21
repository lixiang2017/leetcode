'''
执行用时：246 ms, 在所有 MySQL 提交中击败了94.02% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：15 / 15
'''
# Write your MySQL query statement below
select sell_date,
count(distinct product) as num_sold,
group_concat(distinct product order by product separator ',') as products 
from activities
group by sell_date 
order by sell_date 

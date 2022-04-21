'''
行转列，列转行

执行用时：269 ms, 在所有 MySQL 提交中击败了97.82% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
'''
# Write your MySQL query statement below
select product_id, 'store1' as store, store1 as price 
from products where store1 is not null 
union all 
select product_id, 'store2' as store, store2 as price 
from products where store2 is not null 
union all 
select product_id, 'store3' as store, store3 as price 
from products where store3 is not null 


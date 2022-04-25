'''
执行用时：547 ms, 在所有 MySQL 提交中击败了22.88% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：20 / 20
'''
# Write your MySQL query statement below
select 
customer_number
from orders 
group by customer_number
order by count(order_number) desc limit 1



'''
执行用时：522 ms, 在所有 MySQL 提交中击败了36.14% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：20 / 20
'''
# Write your MySQL query statement below
select customer_number
from orders
group by customer_number 
having count(order_number) >= all(
    select count(order_number)
    from orders 
    group by customer_number
)


'''
执行用时：508 ms, 在所有 MySQL 提交中击败了49.31% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：20 / 20
'''
# Write your MySQL query statement below
select customer_number from (
    select customer_number,
    rank() over (order by count(order_number) desc) as rk 
    from orders 
    group by customer_number 
) t where rk = 1

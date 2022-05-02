'''
执行用时：1166 ms, 在所有 MySQL 提交中击败了84.71% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：15 / 15
'''
# Write your MySQL query statement below
select 
    u.user_id as buyer_id, 
    u.join_date,
    count(o.order_id) as orders_in_2019
from users as u 
left join (
    select * from orders 
    where order_date between '2019-01-01' and '2019-12-31'
) o on u.user_id = o.buyer_id 
group by u.user_id, u.join_date




'''
执行用时：1509 ms, 在所有 MySQL 提交中击败了7.50% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：15 / 15
'''
# Write your MySQL query statement below
select 
    u.user_id as buyer_id, 
    u.join_date,
    if(o.order_id is null, 0, count(o.order_id)) as orders_in_2019
from users as u 
left join (
    select * from orders 
    where order_date between '2019-01-01' and '2019-12-31'
) o on u.user_id = o.buyer_id 
group by u.user_id, u.join_date



'''
执行用时：1177 ms, 在所有 MySQL 提交中击败了78.93% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：15 / 15
'''
# Write your MySQL query statement below
select 
    u.user_id as buyer_id, 
    u.join_date,
    ifnull(count(o.order_id), 0) as orders_in_2019
from users as u 
left join (
    select * from orders 
    where order_date between '2019-01-01' and '2019-12-31'
) o on u.user_id = o.buyer_id 
group by u.user_id, u.join_date








# min
#执行用时：525 ms, 在所有 MySQL 提交中击败了36.69% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# Write your MySQL query statement below
select
    product_id, 
    min(case store when 'store1' then price else null end) as store1,
    min(case store when 'store2' then price else null end) as store2,
    min(case store when 'store3' then price else null end) as store3
from products
group by product_id



# max
#执行用时：826 ms, 在所有 MySQL 提交中击败了5.17% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# Write your MySQL query statement below
select
    product_id, 
    max(case store when 'store1' then price else null end) as store1,
    max(case store when 'store2' then price else null end) as store2,
    max(case store when 'store3' then price else null end) as store3
from products
group by product_id


#sum
#执行用时：545 ms, 在所有 MySQL 提交中击败了21.18% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# Write your MySQL query statement below
select
    product_id, 
    sum(case store when 'store1' then price else null end) as store1,
    sum(case store when 'store2' then price else null end) as store2,
    sum(case store when 'store3' then price else null end) as store3
from products
group by product_id



# min max sum
#执行用时：629 ms, 在所有 MySQL 提交中击败了5.17% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# Write your MySQL query statement below
select
    product_id, 
    min(case store when 'store1' then price else null end) as store1,
    max(case store when 'store2' then price else null end) as store2,
    sum(case store when 'store3' then price else null end) as store3
from products
group by product_id


# avg
#执行用时：600 ms, 在所有 MySQL 提交中击败了5.83% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# Write your MySQL query statement below
select
    product_id, 
    avg(case store when 'store1' then price else null end) as store1,
    avg(case store when 'store2' then price else null end) as store2,
    avg(case store when 'store3' then price else null end) as store3
from products
group by product_id


# group by 1
#执行用时：274 ms, 在所有 MySQL 提交中击败了100.00% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# Write your MySQL query statement below
select
    product_id, 
    min(case store when 'store1' then price else null end) as store1,
    max(case store when 'store2' then price else null end) as store2,
    avg(case store when 'store3' then price else null end) as store3
from products
group by 1  # product_id


# if
#执行用时：271 ms, 在所有 MySQL 提交中击败了100.00% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# Write your MySQL query statement below
select
    product_id, 
    min(if(store='store1', price, null)) as store1,
    max(if(store='store2', price, null)) as store2,
    avg(if(store='store3', price, null)) as store3
from products
group by 1  # product_id


# distinct + left join
#执行用时：560 ms, 在所有 MySQL 提交中击败了12.97% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# Write your MySQL query statement below
select
    distinct
    p.product_id, 
    a.price store1,
    b.price store2,
    c.price store3
from products p
left join
    (select * from products where store = 'store1') a on p.product_id = a.product_id
left join
    (select * from products where store = 'store2') b on p.product_id = b.product_id
left join
    (select * from products where store = 'store3') c on p.product_id = c.product_id


# left join + group by
#执行用时：566 ms, 在所有 MySQL 提交中击败了11.00% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# Write your MySQL query statement below
select
    #distinct
    p.product_id, 
    a.price store1,
    b.price store2,
    c.price store3
from products p
left join
    (select * from products where store = 'store1') a on p.product_id = a.product_id
left join
    (select * from products where store = 'store2') b on p.product_id = b.product_id
left join
    (select * from products where store = 'store3') c on p.product_id = c.product_id
group by 1
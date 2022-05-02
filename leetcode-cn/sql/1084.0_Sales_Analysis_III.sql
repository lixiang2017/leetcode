'''
执行用时：1036 ms, 在所有 MySQL 提交中击败了44.90% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select product_id, product_name 
from product 
where product_id in (
    select distinct product_id 
    from sales
    where sale_date between '2019-01-01' and '2019-03-31'
) and product_id not in (
    select distinct product_id 
    from sales
    where sale_date not between '2019-01-01' and '2019-03-31'
) 


'''
执行用时：1003 ms, 在所有 MySQL 提交中击败了67.97% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select product_id, product_name 
from product 
where product_id in (
    select product_id from (
        select distinct product_id,
        min(sale_date) as min_sale_date,
        max(sale_date) as max_sale_date
        from sales
        group by product_id
    ) t  where min_sale_date between '2019-01-01' and '2019-03-31' and 
         max_sale_date between '2019-01-01' and '2019-03-31'
)


'''
执行用时：1010 ms, 在所有 MySQL 提交中击败了61.93% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：12 / 12
'''
# Write your MySQL query statement below
select p.product_id, p.product_name 
from product p, sales s 
where p.product_id = s.product_id
group by p.product_id 
having sum(sale_date < '2019-01-01') = 0 and sum(sale_date > '2019-03-31') = 0



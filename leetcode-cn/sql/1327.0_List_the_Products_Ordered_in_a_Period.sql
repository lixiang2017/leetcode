
--- 执行用时：696 ms, 在所有 MySQL 提交中击败了12.37% 的用户
--- 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
14 / 14 个通过测试用例
状态：通过
执行用时: 696 ms
内存消耗: 0 B
提交时间：13 分钟前

# Write your MySQL query statement below
select PRODUCT_NAME, UNIT from
(
    select p.product_name as PRODUCT_NAME, sum(o.unit) AS UNIT from Orders o 
    inner join Products p on p.product_id = o.product_id
    where o.order_date >= CAST('2020-02-01' AS DATE) and o.order_date < CAST('2020-03-01' AS DATE)  
    group by o.product_id
) t
where t.unit >= 100


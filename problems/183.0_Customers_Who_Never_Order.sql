# Write your MySQL query statement below
select name as customers from customers where id not in
(
    select customerid from orders
)

# Success
# Details 
# Runtime: 550 ms, faster than 68.04% of MySQL online submissions for Customers Who Never Order.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.



# Write your MySQL query statement below
# left join
select name as customers from  customers
left join orders on customers.id = orders.customerid
where orders.customerid is null

# Success
# Details 
# Runtime: 629 ms, faster than 53.37% of MySQL online submissions for Customers Who Never Order.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.


# Write your MySQL query statement below
# not exists
select name as customers from customers c
where not exists (select * from orders o where o.customerid = c.id)


# Success
# Details 
# Runtime: 439 ms, faster than 96.30% of MySQL online submissions for Customers Who Never Order.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.
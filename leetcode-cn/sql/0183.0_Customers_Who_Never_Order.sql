# Write your MySQL query statement below
# 执行用时：326 ms, 在所有 MySQL 提交中击败了91.25%的用户
# 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
select Name as Customers from Customers c where c.Id not in 
(select CustomerId from Orders)



/* Write your T-SQL query statement below */
# 不加distinct会超时
# 0 / 12 个通过测试用例
# 状态：超出时间限制
# 提交时间：几秒前

# 不过，有时也能通过
# 执行用时：1014 ms, 在所有 mssql 提交中击败了64.50%的用户
# 内存消耗：0 B, 在所有 mssql 提交中击败了100.00%的用户
select Name as Customers from Customers c where c.Id not in 
(select CustomerId from Orders)



/* Write your T-SQL query statement below */
# 执行用时：1290 ms, 在所有 mssql 提交中击败了41.25%的用户
# 内存消耗：0 B, 在所有 mssql 提交中击败了100.00%的用户
select Name as Customers from Customers c where c.Id not in 
(select distinct CustomerId from Orders)


/*
执行用时：623 ms, 在所有 MySQL 提交中击败了14.85% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：11 / 11
*/
# Write your MySQL query statement below
select name as customers from customers 
where id not in (select customerid from orders)


/*
执行用时：592 ms, 在所有 MySQL 提交中击败了26.36% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：11 / 11
*/
# Write your MySQL query statement below
select name as customers from customers c
where not exists (select customerid from orders o where c.id = o.customerid)


/*
执行用时：524 ms, 在所有 MySQL 提交中击败了86.31% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：11 / 11
*/
# Write your MySQL query statement below
select name as customers from customers c
where not exists (select 14234 from orders o where c.id = o.customerid)

/*
执行用时：574 ms, 在所有 MySQL 提交中击败了36.84% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：11 / 11
*/
# Write your MySQL query statement below
select name as customers from customers c
left join orders o on c.id = o.customerid where o.id is null 



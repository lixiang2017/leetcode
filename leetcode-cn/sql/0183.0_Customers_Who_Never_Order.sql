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
select Name as Customers from Customers c where c.Id not in 
(select CustomerId from Orders)



/* Write your T-SQL query statement below */
# 执行用时：1290 ms, 在所有 mssql 提交中击败了41.25%的用户
# 内存消耗：0 B, 在所有 mssql 提交中击败了100.00%的用户
select Name as Customers from Customers c where c.Id not in 
(select distinct CustomerId from Orders)

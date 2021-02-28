# Write your MySQL query statement below
# 执行用时：237 ms, 在所有 MySQL 提交中击败了86.14%的用户
# 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00%的用户
select p.Firstname, p.Lastname, a.City, a.State from Person p left join Address a on p.PersonId = a.PersonId



# MS SQL Server
/* Write your T-SQL query statement below */
# 执行用时：1500 ms, 在所有 mssql 提交中击败了37.60%的用户
# 内存消耗：0 B, 在所有 mssql 提交中击败了100.00%的用户
select p.Firstname, p.Lastname, a.City, a.State from Person p left join Address a on p.PersonId = a.PersonId


# Oracle
/* Write your PL/SQL query statement below */
# 执行用时：1476 ms, 在所有 oraclesql 提交中击败了20.89%的用户
# 内存消耗：0 B, 在所有 oraclesql 提交中击败了100.00%的用户
select p.Firstname, p.Lastname, a.City, a.State from Person p left join Address a on p.PersonId = a.PersonId
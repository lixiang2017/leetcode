/*
执行用时：371 ms, 在所有 MySQL 提交中击败了73.50% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：15 / 15
*/
# Write your MySQL query statement below
select email from
(
    select email, count(*) as freq
    from person
    group by email
) a where freq > 1


/*
执行用时：408 ms, 在所有 MySQL 提交中击败了23.26% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：15 / 15
*/
# Write your MySQL query statement below
select email from person
group by email 
having count(email) > 1



'''
执行用时：398 ms, 在所有 MySQL 提交中击败了63.85% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：15 / 15
'''
# Write your MySQL query statement below
select email from person group by email having count(1) > 1


'''
执行用时：382 ms, 在所有 MySQL 提交中击败了85.01% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：15 / 15
'''
# Write your MySQL query statement below
select email from person group by email having count(2341324) > 1

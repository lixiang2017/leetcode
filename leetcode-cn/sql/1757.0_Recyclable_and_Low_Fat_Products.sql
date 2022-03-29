# 执行用时：688 ms, 在所有 MySQL 提交中击败了5.08% 的用户
# 内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
# 通过测试用例：22 / 22

# Write your MySQL query statement below
select product_id from products where low_fats = 'Y' and recyclable = 'Y'


/*
执行用时：550 ms, 在所有 MySQL 提交中击败了53.05% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select product_id from products where not (low_fats = 'N' or recyclable = 'N') 


/*
执行用时：717 ms, 在所有 MySQL 提交中击败了5.08% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select product_id from products where (low_fats,recyclable) = ('Y', 'Y')


/*
执行用时：641 ms, 在所有 MySQL 提交中击败了8.13% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select product_id 
from products 
where (low_fats,recyclable) <> ('Y', 'N')
and (low_fats,recyclable) <> ('N', 'Y')
and (low_fats,recyclable) <> ('N', 'N')


/*
执行用时：576 ms, 在所有 MySQL 提交中击败了24.94% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select product_id 
from products 
where (low_fats = 'Y') * (recyclable = 'Y')


/*
执行用时：680 ms, 在所有 MySQL 提交中击败了5.08% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select product_id from products where !(low_fats = 'N' or recyclable = 'N') 


/*
执行用时：660 ms, 在所有 MySQL 提交中击败了5.76% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select product_id from products where concat(low_fats, recyclable) = 'YY' 


/*
执行用时：568 ms, 在所有 MySQL 提交中击败了30.02% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
select product_id from products 
where ! (concat(low_fats, recyclable) = 'YN' or concat(low_fats, recyclable) = 'NY' or concat(low_fats, recyclable) = 'NN')



/*
执行用时：579 ms, 在所有 MySQL 提交中击败了23.70% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
with rank_table as (
    select *, rank() over (order by low_fats desc, recyclable desc) r from products 
)
select product_id from rank_table
where r > 
(
    select max(r) from rank_table where (low_fats, recyclable) <> ('Y', 'Y')
)


/*
执行用时：655 ms, 在所有 MySQL 提交中击败了6.32% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
with rank_table as (
    select *, rank() over (order by low_fats desc, recyclable desc) r from products 
)
select product_id from rank_table
where r > 
ifnull( (select max(r) from rank_table where (low_fats, recyclable) <> ('Y', 'Y')), 0)


/*
执行用时：576 ms, 在所有 MySQL 提交中击败了24.94% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：22 / 22
*/
# Write your MySQL query statement below
with rank_table as (
    select *, rank() over (order by low_fats, recyclable) r from products 
)
select product_id from rank_table
where r <
ifnull( 
    (select min(r) from rank_table where (low_fats, recyclable) <> ('Y', 'Y')), 
    (select max(r) + 1 from rank_table)
)







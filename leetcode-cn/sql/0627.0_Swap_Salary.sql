/*
执行用时：257 ms, 在所有 MySQL 提交中击败了35.51% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
update salary set sex = 
case 
when sex = 'm' then 'f'
when sex = 'f' then 'm'
end


/*
执行用时：240 ms, 在所有 MySQL 提交中击败了75.14% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
update salary set sex = if(sex = 'm', 'f', 'm')

/*
执行用时：238 ms, 在所有 MySQL 提交中击败了81.61% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
update salary set sex = char(ascii('m') + ascii('f') - ascii(sex))




/*
执行用时：253 ms, 在所有 MySQL 提交中击败了41.46% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
update salary 
set sex = char(ascii('m') ^ ascii('f') ^ ascii(sex))


/*
执行用时：250 ms, 在所有 MySQL 提交中击败了46.62% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：8 / 8
*/
# Write your MySQL query statement below
update salary 
set sex = trim(sex from "fm")

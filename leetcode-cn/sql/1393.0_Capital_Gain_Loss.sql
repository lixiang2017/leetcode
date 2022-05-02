'''
执行用时：490 ms, 在所有 MySQL 提交中击败了74.91% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：17 / 17
'''
# Write your MySQL query statement below
select 
    stock_name,
    sum(
        case operation when 'Buy' then -price
                        else price
        end 
    ) as capital_gain_loss
from stocks
group by stock_name 



'''
执行用时：511 ms, 在所有 MySQL 提交中击败了49.74% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：17 / 17
'''
# Write your MySQL query statement below
select 
    stock_name,
    sum(
        case when operation = 'Buy' then -price
                        else price
        end 
    ) as capital_gain_loss
from stocks
group by stock_name 


'''
执行用时：489 ms, 在所有 MySQL 提交中击败了75.80% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：17 / 17
'''
# Write your MySQL query statement below
select 
    stock_name,
    sum(if(operation = 'Buy', -price, price)) as capital_gain_loss
from stocks
group by stock_name 


# Write your MySQL query statement below
update salary 
    set sex = 
        case when sex = 'm' then 'f'
             when sex = 'f' then 'm'
        else sex 
        end
# Success
# Details 
# Runtime: 160 ms, faster than 96.92% of MySQL online submissions for Swap Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Swap Salary.
# Write your MySQL query statement below
update salary 
    set sex = (CASE WHEN sex = 'm' THEN 'f' else 'm' END)
# Success
# Details 
# Runtime: 249 ms, faster than 87.77% of MySQL online submissions for Swap Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Swap Salary.
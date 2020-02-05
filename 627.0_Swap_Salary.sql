# Write your MySQL query statement below
update salary set sex = CHAR(ASCII('f') + ASCII('m') - ASCII(sex))
# Success
# Details 
# Runtime: 177 ms, faster than 94.87% of MySQL online submissions for Swap Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Swap Salary.
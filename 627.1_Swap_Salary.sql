# Write your MySQL query statement below
update salary set sex = CHAR(ASCII('f') ^ ASCII('m') ^ ASCII(sex))
# Success
# Details 
# Runtime: 362 ms, faster than 56.42% of MySQL online submissions for Swap Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Swap Salary.
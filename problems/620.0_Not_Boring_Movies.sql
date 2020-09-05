# Write your MySQL query statement below
select id, movie, description, rating from cinema where id % 2 = 1 and description <> 'boring' order by rating desc

# Success
# Details 
# Runtime: 211 ms, faster than 84.95% of MySQL online submissions for Not Boring Movies.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Not Boring Movies.
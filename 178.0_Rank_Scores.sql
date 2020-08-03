# Write your MySQL query statement below
select score, CAST(`Rank` as unsigned) as `Rank` from 
(
    select score, @r := if(@pre = score, @r, @r + 1) as `Rank`, @pre := score from
    (
        select score from Scores, (select @r := 0, @pre := -1) as init order by score desc
    ) as t1
) as t2

Success
Details
Runtime: 302 ms, faster than 73.74% of MySQL online submissions for Rank Scores.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.


# Write your MySQL query statement below
select score, dense_rank() over (order by Score desc) as `Rank` from Scores

Success
Details
Runtime: 289 ms, faster than 78.73% of MySQL online submissions for Rank Scores.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.


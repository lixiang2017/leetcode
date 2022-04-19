# Write your MySQL query statement below
select name from customer where referee_id is null or referee_id != 2


https://stackoverflow.com/questions/21927117/what-is-this-operator-in-mysql
# Write your MySQL query statement below
select name from customer where not referee_id <=> 2


# Write your MySQL query statement below
select name from customer 
where ifnull(referee_id, 0) != 2

# Write your MySQL query statement below
select name from customer 
where ifnull(referee_id, 1) != 2


# Write your MySQL query statement below
select name from customer 
where ifnull(referee_id, -3242) != 2


# Write your MySQL query statement below
select name from customer 
where referee_id <> 2 or referee_id is null 



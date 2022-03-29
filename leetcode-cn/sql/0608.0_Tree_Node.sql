/*
执行用时：459 ms, 在所有 MySQL 提交中击败了83.18% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：19 / 19
*/
# Write your MySQL query statement below
select id,
case when p_id is null then 'Root' 
     when not exists (select t2.p_id p_id from tree t2 where t1.id = t2.p_id) then 'Leaf' 
     else 'Inner'
end as `type`
from tree t1
order by id


/*
这道题教会大家理解not in与null的真实含义.
如果你理解not in与null值, 那么你会解答为何下述语句得出的结果从来不会返回Leaf值.
select
    id,
    case when p_id is null then "Root"
         when id not in (select p_id from tree) then "Leaf"
         else "Inner"
    end as Type
from
    tree

A not in B的原理是拿A表值与B表值做是否不等的比较, 也就是a != b. 在sql中, null是缺失未知值而不是空值(详情请见MySQL reference).
https://dev.mysql.com/doc/refman/8.0/en/working-with-null.html
当你判断任意值a != null时, 官方说, "You cannot use arithmetic comparison operators such as =, <, or <> to test for NULL", 任何与null值的对比都将返回null. 因此返回结果为否,这点可以用代码 select if(1 = null, 'true', 'false')证实.

从上述原理可见, 当询问 id not in (select p_id from tree)时, 因为p_id有null值, 返回结果全为false, 于是跳到else的结果, 返回值为inner. 所以在答案中,leaf结果从未彰显,全被inner取代.


执行用时：479 ms, 在所有 MySQL 提交中击败了48.93% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：19 / 19
*/
# Write your MySQL query statement below
select id,
case when p_id is null then 'Root' 
     when id in (select p_id from tree) then  'Inner'
     else 'Leaf'
end as `type`
from tree
order by id

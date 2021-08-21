#执行用时：590 ms, 在所有 MySQL 提交中击败了100.00% 的用户
#内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户

#ref:
https://leetcode-cn.com/problems/league-statistics/solution/fan-suo-fan-suo-fan-suo-fan-suo-yi-bu-bu-3wm6/

# Write your MySQL query statement below

# create temporary table
With combination as (
# as home team
select home_team_id as team_id, home_team_goals as goal_for, away_team_goals as goal_against, home_team_points as points
from (
    select home_team_id, home_team_goals, away_team_id, away_team_goals,
        case when home_team_goals > away_team_goals then 3
             when home_team_goals = away_team_goals then 1
             else 0 end as home_team_points
    from matches
) A

union all # union all

# as away team
select away_team_id as team_id, away_team_goals as goal_for, home_team_goals as goal_against, away_team_points as points
from (
    select home_team_id, home_team_goals, away_team_id, away_team_goals,
        case when home_team_goals < away_team_goals then 3
             when home_team_goals = away_team_goals then 1
             else 0 end as away_team_points
    from matches
) B
)

# result
select
    team_name,
    count(*) as matches_played,
    sum(points) as points,
    sum(goal_for) as goal_for,
    sum(goal_against) as goal_against,
    sum(goal_for) - sum(goal_against) as goal_diff
from combination inner join teams t using(team_id)
group by team_name
order by points desc, goal_diff desc, team_name


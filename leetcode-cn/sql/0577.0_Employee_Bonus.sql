# Write your MySQL query statement below
select e.name, b.bonus from Employee e left join Bonus b on e.empId = b.empId where b.bonus < 1000 or b.bonus is null


import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, bonus, on="empId", how="left")
    return merged.loc[(merged["bonus"].isna()) | (merged["bonus"] < 1000), ["name", "bonus"]]
    
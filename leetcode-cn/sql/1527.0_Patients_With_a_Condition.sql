'''
执行用时：176 ms, 在所有 MySQL 提交中击败了97.60% 的用户
内存消耗：0 B, 在所有 MySQL 提交中击败了100.00% 的用户
通过测试用例：14 / 14
'''
# Write your MySQL query statement below
select patient_id, patient_name, conditions from patients
where conditions like 'diab1%' or conditions like '% diab1%'

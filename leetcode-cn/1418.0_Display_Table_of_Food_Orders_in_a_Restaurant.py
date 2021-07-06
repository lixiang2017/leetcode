'''
Hash Table + Hash Set

执行用时：596 ms, 在所有 Python3 提交中击败了17.86% 的用户
内存消耗：60.7 MB, 在所有 Python3 提交中击败了5.36% 的用户
'''

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables, foods = set(), set()

        tablefood2cnt = defaultdict(int)
        for customerName, tableNumber, foodItem in orders:
            tables.add(tableNumber)
            foods.add(foodItem)
            tablefood2cnt[(tableNumber, foodItem)] += 1
        
        foods = sorted(list(foods))
        tables = [str(t) for t in sorted([int(table) for table in tables])]
        title = ['Table'] + list(foods)
        display = [title]
        for table in tables:
            one_table = [table]
            for food in foods:
                one_table.append(tablefood2cnt[(table, food)])
            one_table = [str(item) for item in one_table]
            display.append(one_table)

        return display

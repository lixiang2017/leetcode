'''
simulation

执行用时：1396 ms, 在所有 Python3 提交中击败了7.69% 的用户
内存消耗：22 MB, 在所有 Python3 提交中击败了100.00% 的用户
'''


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        unhappy = set()
        for [x, y], [u, v] in permutations(pairs, 2):
            px = preferences[x]
            py = preferences[y]
            pu = preferences[u]
            pv = preferences[v]
            px_y, px_u, px_v = px.index(y), px.index(u), px.index(v)
            py_x, py_u, py_v = py.index(x), py.index(u), py.index(v)
            pu_x, pu_y, pu_v = pu.index(x), pu.index(y), pu.index(v)
            pv_x, pv_y, pv_u = pv.index(x), pv.index(y), pv.index(u)
            # check x, (u <--> v)
            if (px_u < px_y and pu_x < pu_v) or (px_v < px_y and pv_x < pv_u):
                unhappy.add(x)
            # check y, (x <--> y)
            if (py_u < py_x and pu_y < pu_v) or (py_v < py_x and pv_y < pv_u):
                unhappy.add(y)
            # check u, (x <--> u, y <--> v), compare with first
            if (pu_x < pu_v and px_u < px_y) or (pu_y < pu_v and py_u < py_x):
                unhappy.add(u)
            # check v, (u <--> v), compare with check u
            if (pv_x < pv_u and px_v < px_y) or (pv_y < pv_u and py_v < py_x):
                unhappy.add(v) 
        return len(unhappy)

'''
simulation

执行用时：1328 ms, 在所有 Python3 提交中击败了7.69% 的用户
内存消耗：21.9 MB, 在所有 Python3 提交中击败了100.00% 的用户
'''


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        unhappy, checked = set(), set()
        N = len(preferences)
        for [x, y], [u, v] in permutations(pairs, 2):
            if len(checked) == N:
                break
            px = preferences[x]
            py = preferences[y]
            pu = preferences[u]
            pv = preferences[v]
            px_y, px_u, px_v = px.index(y), px.index(u), px.index(v)
            py_x, py_u, py_v = py.index(x), py.index(u), py.index(v)
            pu_x, pu_y, pu_v = pu.index(x), pu.index(y), pu.index(v)
            pv_x, pv_y, pv_u = pv.index(x), pv.index(y), pv.index(u)
            # check x, (u <--> v)
            if x not in checked:
                if (px_u < px_y and pu_x < pu_v) or (px_v < px_y and pv_x < pv_u):
                    unhappy.add(x)
                    checked.add(x)
            # check y, (x <--> y)
            if y not in checked:
                if (py_u < py_x and pu_y < pu_v) or (py_v < py_x and pv_y < pv_u):
                    unhappy.add(y)
                    checked.add(y)
            # check u, (x <--> u, y <--> v), compare with first
            if u not in checked:
                if (pu_x < pu_v and px_u < px_y) or (pu_y < pu_v and py_u < py_x):
                    unhappy.add(u)
                    checked.add(u)
            # check v, (u <--> v), compare with check u
            if v not in checked:
                if (pv_x < pv_u and px_v < px_y) or (pv_y < pv_u and py_v < py_x):
                    unhappy.add(v) 
                    checked.add(v)
        return len(unhappy)


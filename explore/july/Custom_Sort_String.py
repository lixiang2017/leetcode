'''
Hash Table + Hash Set

You are here!
Your runtime beats 62.80 % of python3 submissions.
You are here!
Your memory usage beats 52.49 % of python3 submissions.
'''
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        not_seen = ''
        order_set = set(list(order))
        seen = defaultdict(int)
        for ch in str:
            if ch in order_set:
                seen[ch] += 1
            else:
                not_seen += ch
        
        return ''.join(ch * seen[ch] for ch in order) + not_seen


'''
You are here!
Your runtime beats 99.22 % of python3 submissions.
'''
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        o2idx = {ch: i for i, ch in enumerate(order)}
        order_set = set(list(order))
        return ''.join(sorted(list(str), key=lambda ch: o2idx[ch] if ch in order_set else -1))



'''
You are here!
Your runtime beats 62.80 % of python3 submissions.
You are here!
Your memory usage beats 52.49 % of python3 submissions.
'''
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        t = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(str, key=lambda c: t.get(c, 26)))


'''
You are here!
Your runtime beats 96.59 % of python3 submissions.
'''
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        count = Counter(list(str))
        return ''.join(c * count[c] for c in order) + ''.join(c * count[c] for c in count if c not in order)

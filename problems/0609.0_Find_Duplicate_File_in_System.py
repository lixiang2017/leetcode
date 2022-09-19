'''
hash table

Runtime: 197 ms, faster than 24.58% of Python3 online submissions for Find Duplicate File in System.
Memory Usage: 24 MB, less than 54.58% of Python3 online submissions for Find Duplicate File in System.
'''
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_paths = defaultdict(list)
        for path in paths:
            parts = path.split()
            prefix = parts[0]
            for f in parts[1:]:
                idx = f.index('(')
                full_name = prefix + '/' + f[: idx]
                content = f[idx + 1: -1]
                content_paths[content].append(full_name)
        return [paths for c, paths in content_paths.items() if len(paths) > 1]

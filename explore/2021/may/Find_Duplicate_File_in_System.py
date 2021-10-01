'''
approach: Hash Table
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 17.27 % of python3 submissions.
You are here!
Your memory usage beats 69.67 % of python3 submissions.
'''

import re

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content2paths = defaultdict(list)
        for path in paths:
            parts = path.split()
            N = len(parts)
            # parts[0]
            for i in range(1, N):
                # parts[i]
                file_name, content, _ = re.split('\(|\)', parts[i])
                content2paths[content].append(parts[0] + '/' + file_name)
    
        duplicates = []
        for _, paths in content2paths.items():
            if len(paths) >= 2:
                duplicates.append(paths)
        
        return duplicates

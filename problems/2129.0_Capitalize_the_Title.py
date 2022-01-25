'''
Runtime: 32 ms, faster than 87.38% of Python3 online submissions for Capitalize the Title.
Memory Usage: 14.4 MB, less than 13.21% of Python3 online submissions for Capitalize the Title.
'''
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(w.title() if len(w) > 2 else w.lower() for w in title.split())


'''
Runtime: 43 ms, faster than 55.81% of Python3 online submissions for Capitalize the Title.
Memory Usage: 14.2 MB, less than 75.35% of Python3 online submissions for Capitalize the Title.
'''
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(w.capitalize() if len(w) > 2 else w.lower() for w in title.split())
        
'''
sort + two pointers
T: O(NlogN + len(searchWord) + N)
S: O(3 * len(searchWord))

Runtime: 179 ms, faster than 63.40% of Python3 online submissions for Search Suggestions System.
Memory Usage: 17.1 MB, less than 84.09% of Python3 online submissions for Search Suggestions System.
'''
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        j, n, ans = 0, len(products), []
        cur = ''
        for i, ch in enumerate(searchWord):
            cur += ch 
            while j < n and products[j] < cur:
                j += 1
            hints = []
            for idx in [j, j + 1, j + 2]:
                if idx < n and products[idx][: i + 1] == cur:
                    hints.append(products[idx])
            ans.append(hints)       
        return ans 
    
        
'''
# filter just starts with searchWord[0]

Runtime: 79 ms, faster than 97.11% of Python3 online submissions for Search Suggestions System.
Memory Usage: 17 MB, less than 84.09% of Python3 online submissions for Search Suggestions System.
'''
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # filter just starts with searchWord[0]
        products = [p for p in products if p[0] == searchWord[0]]
        products.sort()
        j, n, ans = 0, len(products), []
        cur = ''
        for i, ch in enumerate(searchWord):
            cur += ch 
            while j < n and products[j] < cur:
                j += 1
            hints = []
            for idx in [j, j + 1, j + 2]:
                if idx < n and products[idx][: i + 1] == cur:
                    hints.append(products[idx])
            ans.append(hints)       
        return ans 
    
        


'''
approach: Sort + Hash Table
Time: O(sort) + O(total length of products and searchWord), O(sort) + O(2 * 10^4 + 1000)
Space: O(3 * total length of products), O(3 * 2 * 10 ^ 4)

You are here!
Your runtime beats 63.82 % of python3 submissions.
You are here!
Your memory usage beats 41.98 % of python3 submissions
'''
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggest = defaultdict(list)
        for product in products:
            L = len(product)
            for i in range(1, L + 1):
                if len(suggest[product[: i]]) < 3:
                    suggest[product[: i]].append(product)
        
        suggested = []
        N = len(searchWord)
        for i in range(1, N + 1):
            suggested.append(suggest[searchWord[: i]])
        return suggested

'''
approach: Sort + Hash Table
Time: O(sort) + O(total length of products and searchWord), O(sort) + O(2 * 10^4 + 1000)
Space: O(3 * total length of products), O(3 * 2 * 10 ^ 4)

You are here!
Your runtime beats 60.34 % of python3 submissions.
You are here!
Your memory usage beats 41.98 % of python3 submissions.
'''

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggest = defaultdict(list)
        for product in products:
            for i in range(1, len(product) + 1):
                if len(suggest[product[: i]]) < 3:
                    suggest[product[: i]].append(product)
        
        return [suggest[searchWord[: i]] for i in range(1, len(searchWord) + 1)]





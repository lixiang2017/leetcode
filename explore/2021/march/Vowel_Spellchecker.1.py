'''
approach: Binary Search + Sort + Dict
Time: O( MlogM + MlogM + (logM + logM + M) * N )  
Space: O(M + M)

53 / 53 test cases passed.
Status: Accepted
Runtime: 8868 ms
Memory Usage: 16.3 MB
Submitted: 0 minutes ago

You are here!
Your memory usage beats 30.00 % of python submissions.
'''



class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        M, N = len(wordlist), len(queries)
        capital = [(word.lower(), i) for i, word in enumerate(wordlist)]
        capital.sort()
        map2a = {'e': 'a', 'i': 'a', 'o': 'a', 'u': 'a'}
        errors = [(''.join(map(lambda ch: map2a.get(ch, ch), cap[0])), cap[1]) for i, cap in enumerate(capital)]
        errors.sort()

        corrects = []
        
        for i in range(N):
            found = False
            # origin
            for j in range(M):
                if queries[i] == wordlist[j]:
                    corrects.append(wordlist[j])
                    found = True
                    break
            if found:
                continue

            # capital
            idx = self.binarysearch(capital, 0, M - 1, queries[i].lower())
            if -1 != idx:
                corrects.append(wordlist[idx])
                continue
                                    
            # errors
            qerror = ''.join(map(lambda ch: map2a.get(ch, ch), queries[i].lower()))
            idx = self.binarysearch(errors, 0, M - 1, qerror)
            if -1 != idx:
                corrects.append(wordlist[idx])
                continue

            if not found:
                corrects.append('')  

        return corrects

    def binarysearch(self, patterns, left, right, query):
        if left > right:
            return -1

        mid = (left + right) / 2
        if patterns[mid][0] == query:
            while mid - 1 >= 0 and patterns[mid][0] == patterns[mid - 1][0]:
                mid -= 1
            return patterns[mid][1]
        elif patterns[mid][0] > query:
            return self.binarysearch(patterns, left, mid - 1, query)
        else:
            return self.binarysearch(patterns, mid + 1, right, query)




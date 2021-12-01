'''
Union Find

Runtime: 296 ms, faster than 30.81% of Python3 online submissions for Accounts Merge.
Memory Usage: 17.4 MB, less than 99.79% of Python3 online submissions for Accounts Merge.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.name = [''] * n
        self.mailsp = dict()

    def find(self, x):
        while x != self.p[x]:
            self.p[x] = self.find(self.p[x])
            x = self.p[x]
        return x
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = self.p[py]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UF(n)
        for i, acc in enumerate(accounts):
            name, mails = acc[0], acc[1: ]
            for mail in mails:
                uf.name[i] = name
                if mail not in uf.mailsp:
                    uf.mailsp[mail] = i
                else:
                    uf.union(uf.mailsp[mail], i)
        parents = set(uf.find(i) for i in range(n))
        ans = []
        for p in parents:
            name = uf.name[p]
            mails = []
            for mail, i in uf.mailsp.items():
                if uf.find(i) == p:
                    mails.append(mail)
            mails.sort()
            ans.append([name] + mails)
        
        return ans


'''
Union Find
use seen set

Runtime: 272 ms, faster than 36.19% of Python3 online submissions for Accounts Merge.
Memory Usage: 18.2 MB, less than 81.74% of Python3 online submissions for Accounts Merge.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.name = [''] * n
        self.mailsp = dict()

    def find(self, x):
        while x != self.p[x]:
            self.p[x] = self.find(self.p[x])
            x = self.p[x]
        return x
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = self.p[py]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UF(n)
        for i, acc in enumerate(accounts):
            name, mails = acc[0], acc[1: ]
            for mail in mails:
                uf.name[i] = name
                if mail not in uf.mailsp:
                    uf.mailsp[mail] = i
                else:
                    uf.union(uf.mailsp[mail], i)
        parents = set(uf.find(i) for i in range(n))
        ans = []
        seen = set()
        for p in parents:
            name = uf.name[p]
            mails = []
            for mail, i in uf.mailsp.items():
                if mail not in seen and uf.find(i) == p:
                    mails.append(mail)
                    seen.add(mail)
            mails.sort()
            ans.append([name] + mails)
        
        return ans

'''
Runtime: 172 ms, faster than 99.78% of Python3 online submissions for Accounts Merge.
Memory Usage: 18.2 MB, less than 81.74% of Python3 online submissions for Accounts Merge.
'''
class Person:
    def __init__(self, name):
        self.parent: Person = None
        self.name = name
        self.emails: Set[str] = set()
    
    def get_root(self) -> Any:
        current = self
        while current.parent is not None:
            current = current.parent
        return current
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail2person: Dict[str, Person] = {}
        persons: List[Person] = []
        output: List[List[str]] = []
        
        for account in accounts:
            name = account[0]
            mails = account[1: ]
            person: Person = None
            for mail in mails:
                if mail in mail2person:
                    _person = mail2person[mail].get_root()
                    if person is None:
                        person = _person
                    elif person.emails is _person.emails:
                        continue
                    else:
                        person.emails.update(_person.emails)
                        _person.emails.clear()
                        _person.parent = person
                
            if person is None:
                person = Person(name)
                persons.append(person)
            
            for mail in mails:
                mail2person[mail] = person    
                person.emails.add(mail)
                
        for person in persons:
            if person.get_root() is person:
                output.append([person.name] + sorted(person.emails))
            
        return output


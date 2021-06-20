'''
DFS

44 / 49 个通过测试用例
状态：超出时间限制
提交时间：1 分钟内
'''


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingdom = Member(kingName)

    def birth(self, parentName: str, childName: str) -> None:
        def dfs(member):
            if not member:
                return
            if member.name == parentName:
                member.children.append(Member(childName))
                return

            for child in member.children:
                dfs(child)

        dfs(self.kingdom)

    def death(self, name: str) -> None:
        def dfs(member):
            if not member:
                return
            if member.name == name:
                member.isAlive = False
            
            for child in member.children:
                dfs(child)
        
        dfs(self.kingdom)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(member):
            if not member:
                return []

            preorder = [member.name] if member.isAlive else []
            for child in member.children:
                preorder += dfs(child)
            return preorder

        return dfs(self.kingdom)


class Member:
    def __init__(self, name, isAlive=True):
        self.name = name
        self.isAlive = True
        self.children = []


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()



'''
N-ary Tree + Hash Table + Hash Set + Preorder

Time:
ThroneInheritance(kingName): O(1)
birth(parentName, childName): O(1)
death(name): O(1)
getInheritanceOrder: O(N)
Space:
O(N)

执行用时：500 ms, 在所有 Python3 提交中击败了87.50% 的用户
内存消耗：64.1 MB, 在所有 Python3 提交中击败了66.07% 的用户
'''

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.edges = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.edges[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def preorder(name):
            if name not in self.dead:
                ans.append(name)
            
            if name in self.edges:
                for child in self.edges[name]:
                    preorder(child)

        preorder(self.king)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
'''
stack

Runtime: 222 ms, faster than 79.15% of Python3 online submissions for Design Browser History.
Memory Usage: 16.7 MB, less than 70.44% of Python3 online submissions for Design Browser History.
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.q = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        if len(self.q) != self.idx + 1:
            self.q[self.idx + 1: ] = []
        self.q.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx -= min(steps, self.idx)
        return self.q[self.idx]

    def forward(self, steps: int) -> str:
        self.idx += min(steps, len(self.q) - (self.idx + 1))        
        return self.q[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


'''
stack, del

执行用时：136 ms, 在所有 Python3 提交中击败了94.12% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了23.53% 的用户
通过测试用例：72 / 72
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.q = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        del self.q[self.idx + 1: ]
        self.q.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx -= min(steps, self.idx)
        return self.q[self.idx]

    def forward(self, steps: int) -> str:
        self.idx += min(steps, len(self.q) - (self.idx + 1))        
        return self.q[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



'''
Doubly-Linked List

Runtime: 282 ms, faster than 50.54% of Python3 online submissions for Design Browser History.
Memory Usage: 16.8 MB, less than 37.23% of Python3 online submissions for Design Browser History.
'''
class Page:
    def __init__(self, url: str, pre = None, nxt = None) -> None:
        self.url = url
        self.pre = pre
        self.next = nxt
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.cur = Page(homepage)

    def visit(self, url: str) -> None:
        page = Page(url)
        if self.cur.next:
            self.cur.next.pre = None
        # TODO, delete next nodes
        self.cur.next = page
        page.pre = self.cur
        self.cur = page

    def back(self, steps: int) -> str:
        while steps and self.cur.pre:
            self.cur = self.cur.pre
            steps -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



'''
Doubly-Linked List, delete next nodes

执行用时：188 ms, 在所有 Python3 提交中击败了32.35% 的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了62.94% 的用户
通过测试用例：72 / 72
'''
class Page:
    def __init__(self, url: str, pre = None, nxt = None) -> None:
        self.url = url
        self.pre = pre
        self.next = nxt
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.cur = Page(homepage)

    def visit(self, url: str) -> None:
        page = Page(url)
        if self.cur.next:
            self.cur.next.pre = None
        # delete next nodes
        tail = self.cur.next 
        while tail:
            ttail = tail.next 
            del tail 
            tail = ttail
        # set correct pointers
        self.cur.next = page
        page.pre = self.cur
        self.cur = page

    def back(self, steps: int) -> str:
        while steps and self.cur.pre:
            self.cur = self.cur.pre
            steps -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


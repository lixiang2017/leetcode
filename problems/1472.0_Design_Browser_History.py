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

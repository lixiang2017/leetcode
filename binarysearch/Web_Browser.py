'''
Your code took 174 milliseconds — faster than 96.04% in Python
'''

class WebBrowser:
    def __init__(self, homepage):
        self.history = [homepage]
        self.i = 0

    def visit(self, page):
        self.history[self.i + 1 :] = [page]
        self.i += 1

    def back(self, n):
        if n >= self.i:
            self.i = 0
        else:
            self.i -= n
        return self.history[self.i]

    def forward(self, n):
        if self.i + n + 1 >= len(self.history):
            self.i = len(self.history) - 1

        else:
            self.i += n
        return self.history[self.i]



'''
Your code took 213 milliseconds — faster than 73.57% in Python
'''
class WebBrowser:
    def __init__(self, homepage):
        self.history = [homepage]
        self.i = 0

    def visit(self, page):
        self.history[self.i + 1 :] = [page]
        self.i += 1

    def back(self, n):
        self.i = max(0, self.i - n)
        return self.history[self.i]

    def forward(self, n):
        self.i = min(len(self.history) - 1, self.i + n)
        return self.history[self.i]


def solution(x, y):
    # Your code here
    x, y = set(x), set(y)
    if len(x) < len(y):
        x, y = y, x
    return list(x - y)[0]
    
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        solve, skip = [0] * n, [0] * n
        for i, (points, brainpower) in enumerate(questions):
            if i > 0:
                skip[i] = max(skip[i - 1], skip[i])
            solve[i] = skip[i] + points
            if i + brainpower + 1 < n:
                skip[i + brainpower + 1] = max(skip[i + brainpower + 1], skip[i] + points)
        return max(solve + skip)

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        f = [0] * (n + 1)
        for i, (point, brainpower) in enumerate(questions):
            f[i + 1] = max(f[i + 1], f[i])
            j = min(i + brainpower + 1, n)
            f[j] = max(f[j], f[i] + point)
        return f[n]

        
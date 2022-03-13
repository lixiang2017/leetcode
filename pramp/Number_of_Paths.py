'''
Time: 26ms
Passed: 6
Failed: 0
'''
def num_of_paths_to_dest(n):
  path = [[0] * n for _ in range(n)]
  path[0] = [1] * n 
  
  for r in range(1, n):
    for c in range(r, n):
      if r <= c:
        path[r][c] = path[r - 1][c] + path[r][c - 1]
  
  return path[n - 1][n - 1]


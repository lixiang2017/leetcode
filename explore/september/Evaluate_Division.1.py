'''
Floyd

You are here!
Your runtime beats 27.33 % of python submissions.
'''



class Solution(object):
    def calcEquation(self, edges, weights, pairs):

        graph = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))

        for (i, j), weight in itertools.izip(edges, weights):
            graph[i][i], graph[i][j], graph[j][i], graph[j][j] = 1., weight, 1. / weight, 1.

        for mid in graph:
            for i in graph[mid]:
                for j in graph[mid]:
                    graph[i][j] = min(graph[i][j], graph[i][mid] * graph[mid][j])

        return [graph[i][j] if graph[i][j] < float('inf') else -1. for i, j in pairs]

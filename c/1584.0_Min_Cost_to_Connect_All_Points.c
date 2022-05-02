/*
执行用时：280 ms, 在所有 C 提交中击败了61.40% 的用户
内存消耗：33.8 MB, 在所有 C 提交中击败了50.88% 的用户
通过测试用例：72 / 72
*/
void swap(int* a, int* b) {
    int tmp = *a;
    *a = *b, *b = tmp;
}

struct Edge {int len, x, y; };
// asc
int cmp(struct Edge* a, struct Edge* b) { return a->len - b->len; };
int find(int* f, int x) {
    return f[x] == x ? x : (f[x] = find(f, f[x]));
}
int unionSet(int* f, int* rank, int x, int y) {
    int fx = find(f, x), fy = find(f, y);
    if (fx == fy) {
        return false;
    }
    // make sure size_fx >= size_fy, so fy -> fx
    if (rank[fx] < rank[fy]) {
        swap(&fx, &fy);
    }
    rank[fx] += rank[fy];
    f[fy] = fx;
    return true;
}

int minCostConnectPoints(int** points, int pointsSize, int* pointsColSize){
    int n = pointsSize;
    struct Edge edges[(n + 1) * n / 2];
    int edgesSize = 0;
    int cost = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            edges[edgesSize].x = i;
            edges[edgesSize].y = j;
            int weight = fabs(points[i][0] - points[j][0]) + fabs(points[i][1] - points[j][1]);
            edges[edgesSize++].len = weight;
        }
    }
    qsort(edges, edgesSize, sizeof(struct Edge), cmp);
    int f[n], rank[n];
    for (int i = 0; i < n; i++) {
        f[i] = i;
        rank[i] = i;
    }
    int num = 1;
    for (int i = 0; i < edgesSize; i++) {
        if (unionSet(f, rank, edges[i].x, edges[i].y)) {
            cost += edges[i].len;
            num++;
            if (num == n)
                break;
        }
    }
    return cost; 
}

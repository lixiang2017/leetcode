/*
hash table

执行用时：500 ms, 在所有 C 提交中击败了100.00% 的用户
内存消耗：77.9 MB, 在所有 C 提交中击败了27.78% 的用户
通过测试用例：38 / 38
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmp(const void* a1, const void* a2) {
    if ((*(int**)a1)[0] != (*(int**)a2)[0]) {
        return (*(int**)a1)[0] - (*(int**)a2)[0];
    }
    return (*(int**)a1)[1] - (*(int**)a2)[1];
}

struct Node {
    int id;
    int active_cnt;
    struct Node* next;
};

#define HASH_SIZE 32768

int* findingUsersActiveMinutes(int** logs, int logsSize, int* logsColSize, int k, int* returnSize){
    qsort(logs, logsSize, sizeof(int*), cmp);

    struct Node* hash = calloc(HASH_SIZE, sizeof(struct Node));
    for (int i = 0; i < HASH_SIZE; i++) hash[i].id = -1;

    hash[logs[0][0] & (HASH_SIZE - 1)].id = logs[0][0];
    hash[logs[0][0] & (HASH_SIZE - 1)].active_cnt = 1;

    for (int i = 1; i < logsSize; i++) {
        if (logs[i][0] == logs[i - 1][0] && logs[i][1] == logs[i - 1][1]) continue;

        int hash_idx = logs[i][0] & (HASH_SIZE - 1);
        while (hash[hash_idx].id != -1 && hash[hash_idx].id != logs[i][0]) {
            hash_idx++;
            if (hash_idx >= HASH_SIZE) hash_idx -= HASH_SIZE;
        }
        if (hash[hash_idx].id == -1) {
            hash[hash_idx].id = logs[i][0];
            hash[hash_idx].active_cnt = 1;
        } else {
            hash[hash_idx].active_cnt++;
        }
    }

    int* ans = calloc(k, sizeof(int));
    *returnSize = k;
    for (int i = 0; i < HASH_SIZE; i++) {
        if (hash[i].id != -1) {
            ans[hash[i].active_cnt - 1]++;
        }
    }
    free(hash);
    return ans;
}



/*
#define HASH_SIZE 16384

执行用时：524 ms, 在所有 C 提交中击败了83.33% 的用户
内存消耗：67.4 MB, 在所有 C 提交中击败了27.78% 的用户
通过测试用例：38 / 38
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmp(const void* a1, const void* a2) {
    if ((*(int**)a1)[0] != (*(int**)a2)[0]) {
        return (*(int**)a1)[0] - (*(int**)a2)[0];
    }
    return (*(int**)a1)[1] - (*(int**)a2)[1];
}

struct Node {
    int id;
    int active_cnt;
    struct Node* next;
};

#define HASH_SIZE 16384

int* findingUsersActiveMinutes(int** logs, int logsSize, int* logsColSize, int k, int* returnSize){
    qsort(logs, logsSize, sizeof(int*), cmp);

    struct Node* hash = calloc(HASH_SIZE, sizeof(struct Node));
    for (int i = 0; i < HASH_SIZE; i++) hash[i].id = -1;

    hash[logs[0][0] & (HASH_SIZE - 1)].id = logs[0][0];
    hash[logs[0][0] & (HASH_SIZE - 1)].active_cnt = 1;

    for (int i = 1; i < logsSize; i++) {
        if (logs[i][0] == logs[i - 1][0] && logs[i][1] == logs[i - 1][1]) continue;

        int hash_idx = logs[i][0] & (HASH_SIZE - 1);
        while (hash[hash_idx].id != -1 && hash[hash_idx].id != logs[i][0]) {
            hash_idx++;
            if (hash_idx >= HASH_SIZE) hash_idx -= HASH_SIZE;
        }
        if (hash[hash_idx].id == -1) {
            hash[hash_idx].id = logs[i][0];
            hash[hash_idx].active_cnt = 1;
        } else {
            hash[hash_idx].active_cnt++;
        }
    }

    int* ans = calloc(k, sizeof(int));
    *returnSize = k;
    for (int i = 0; i < HASH_SIZE; i++) {
        if (hash[i].id != -1) {
            ans[hash[i].active_cnt - 1]++;
        }
    }
    free(hash);
    return ans;
}




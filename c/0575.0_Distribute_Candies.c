/*
执行用时：188 ms, 在所有 C 提交中击败了54.74% 的用户
内存消耗：9.5 MB, 在所有 C 提交中击败了98.54% 的用户
通过测试用例：206 / 206
*/

int distributeCandies(int* candyType, int candyTypeSize){
    char bits[25001] = {0};
    int t = 0, count = 0;
    for (int i = 0; i < candyTypeSize; i++) {
        t = (candyType[i] + 100000);
        bits[t / 8] |= 1 << (t % 8);
    }
    for (int i = 0; i < 25001; i++) {
        for (int j = 0; j < 8; j++) {
            count += (bits[i] >> j) & 1;
        }
    }
    return count < candyTypeSize/2 ? count : candyTypeSize/2;
}


/*
执行用时：120 ms, 在所有 C 提交中击败了98.91% 的用户
内存消耗：9.7 MB, 在所有 C 提交中击败了94.53% 的用户
通过测试用例：206 / 206
*/

int distributeCandies(int* candyType, int candyTypeSize){
    char bits[25001] = {0};
    int t = 0, count = candyTypeSize;
    for (int i = 0; i < candyTypeSize; i++) {
        t = (candyType[i] + 100000);
        if (bits[t/8] & (1 << (t % 8))) {
            count--;
            continue;
        }
        bits[t / 8] |= 1 << (t % 8);
    }
    return count < candyTypeSize/2 ? count : candyTypeSize/2;
}

/*
执行用时：0 ms, 在所有 C 提交中击败了100.00% 的用户
内存消耗：5.5 MB, 在所有 C 提交中击败了41.55% 的用户
通过测试用例：550 / 550
*/

bool detectCapitalUse(char * word){
    // to record last postions for upper char and lower char
    int lastUpperCharIndex = -1;
    int lastLowerCharIndex = -1;
    int index = 0;
    while (word[index]) {
        if (word[index] >= 'a' && word[index] <= 'z') {
            lastLowerCharIndex = index;
        } else {
            lastUpperCharIndex = index;
        }
        index++;
    }

    if (lastLowerCharIndex >= 0 && lastUpperCharIndex >= 1) {
        return false;
    }
    return true;
}



/*
这三种情况其实可以简化成两种情况
1、全大写
2、除首字母外全小写
ASCII   HEX   BIN
space   20    0010 0000
A       41    0100 0001
Z       5A    0101 1010  
a       61    0110 0001
z       7A    0111 1010
之所以选择空格，是因为空格的那个bit（第六位）可以区分大小写。
1、～a & ‘ ’ 表示全为大写。即空格那一位全为0，用或（a |= *p）, 不能用与。是因为大写的那个位的特征为0.
2、b & ' ' 表示除首字母外全小写。所以用与（b &= *p）. 是因为小写的那个位的特征为1.

执行用时：0 ms, 在所有 C 提交中击败了100.00% 的用户
内存消耗：5.4 MB, 在所有 C 提交中击败了71.98% 的用户
通过测试用例：550 / 550

*/
bool detectCapitalUse(char * word){
    char a = *word, b = 0xff;
    for (char* p=word+1; *p; ++p) {
        a |= *p;
        b &= *p;
    }
    return (~a | b) & ' ';
}

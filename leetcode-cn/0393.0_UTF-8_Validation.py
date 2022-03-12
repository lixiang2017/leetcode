'''
simulation, T: O(N), S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了96.64% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了83.22% 的用户
通过测试用例：49 / 49
'''
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        '''
    Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx  
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

0xxxxxxx                 0 -- 127
110xxxxx  128+64=192       -- 128+64+31=223
1110xxxx  128+64+32=224    -- 128+64+32+15=239
11110xxx  128+64+32+16=240 -- 128+64+32+16+7=247
10xxxxxx  128              -- 128+63=191
        '''
        n = len(data)
        i = 0
        while i < n:
            # UTF8 begins
            if 0 <= data[i] <= 127:
                i += 1
            elif 192 <= data[i] <= 223:
                if i + 1 < n and 128 <= data[i + 1] <= 191:
                    i += 2
                else:
                    return False 
            elif 224 <= data[i] <= 239:
                if i + 2 < n and 128 <= data[i + 1] <= 191 and 128 <= data[i + 2] <= 191:
                    i += 3
                else:
                    return False 
            elif 240 <= data[i] <= 247:
                if i + 3 < n and 128 <= data[i + 1] <= 191 and \
                        128 <= data[i + 2] <= 191 and 128 <= data[i + 3] <= 191:
                    i += 4
                else:
                    return False 
            else:
                return False 

        return True


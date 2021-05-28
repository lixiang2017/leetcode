'''
approach: Bit Manipulation + Dict
Time: O(N * W + N^2)
Space: O(N)

You are here!
Your runtime beats 85.88 % of python3 submissions.
You are here!
Your memory usage beats 85.88 % of python3 submissions.
'''


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
        nums = defaultdict(int)
        for word in words:
            L = len(word)
            num = 0
            for ch in word:
                num |= (1 << (ord(ch) - ord('a')))
                
            # nums[num] = L  # wrong
            nums[num] = max(nums[num], L)
        
        for num1, L1 in nums.items():
            for num2, L2 in nums.items():
                if num1 & num2 == 0:
                    maximum = max(maximum, L1 * L2)
        
        return maximum        

    
'''
Input: ["bdcecbcadca","caafd","bcadc","eaedfcd","fcdecf","dee","bfedd","ffafd","eceaffa","caabe","fbdb","acafbccaa","cdc","ecfdebaafde","cddbabf","adc","cccce","cbbe","beedf","fafbfdcb","ceecfabedbd","aadbedeaf","cffdcfde","fbbdfdccce","ccada","fb","fa","ec","dddafded","accdda","acaad","ba","dabe","cdfcaa","caadfedd","dcdcab","fadbabace","edfdb","dbaaffdfa","efdffceeeb","aefdf","fbadcfcc","dcaeddd","baeb","beddeed","fbfdffa","eecacbbd","fcde","fcdb","eac","aceffea","ebabfffdaab","eedbd","fdeed","aeb","fbb","ad","bcafdabfbdc","cfcdf","deadfed","acdadbdcdb","fcbdbeeb","cbeb","acbcafca","abbcbcbaef","aadcafddf","bd","edcebadec","cdcbabbdacc","adabaea","dcebf","ffacdaeaeeb","afedfcadbb","aecccdfbaff","dfcfda","febb","bfffcaa","dffdbcbeacf","cfa","eedeadfafd","fcaa","addbcad","eeaaa","af","fafc","bedbbbdfae","adfecadcabe","efffdaa","bafbcbcbe","fcafabcc","ec","dbddd","edfaeabecee","fcbedad","abcddfbc","afdafb","afe","cdad","abdffbc","dbdbebdbb"]
Output: 36
Expected: 45
'''



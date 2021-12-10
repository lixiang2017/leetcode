
'''
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = Counter(filter(str.isalpha, licensePlate.lower()))
        return min(filter(lambda w: not (licensePlate - Counter(w.lower())), words), key=len)
'''

from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        print('-----------------------------------')
        pc = Counter(filter(str.isalpha, licensePlate.lower()))
        print('pc: ', pc)
        diff = []
        for w in words:
            wc = Counter(w.lower())
            delta = pc - wc
            print('w: ', w, wc)
            print('delta: ', delta)

        print('filtered: ', list(filter(lambda w: not (pc - Counter(w.lower())), words)))
        return min(filter(lambda w: not (pc - Counter(w.lower())), words), key=len)


def main():
    licensePlate = "1s3 PSt"
    words = ["step","steps","stripe","stepple"]
    Solution().shortestCompletingWord(licensePlate, words)

    licensePlate = "1s3 456"
    words = ["looks","pest","stew","show"]
    Solution().shortestCompletingWord(licensePlate, words)

    licensePlate = "Ah71752"
    words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
    Solution().shortestCompletingWord(licensePlate, words)

    licensePlate = "OgEu755"
    words = ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]
    Solution().shortestCompletingWord(licensePlate, words)

    licensePlate = "iMSlpe4"
    words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
    Solution().shortestCompletingWord(licensePlate, words)

main()



'''
-----------------------------------
pc:  Counter({'s': 2, 'p': 1, 't': 1})
w:  step Counter({'s': 1, 't': 1, 'e': 1, 'p': 1})
delta:  Counter({'s': 1})
w:  steps Counter({'s': 2, 't': 1, 'e': 1, 'p': 1})
delta:  Counter()
w:  stripe Counter({'s': 1, 't': 1, 'r': 1, 'i': 1, 'p': 1, 'e': 1})
delta:  Counter({'s': 1})
w:  stepple Counter({'e': 2, 'p': 2, 's': 1, 't': 1, 'l': 1})
delta:  Counter({'s': 1})
filtered:  ['steps']
-----------------------------------
pc:  Counter({'s': 1})
w:  looks Counter({'o': 2, 'l': 1, 'k': 1, 's': 1})
delta:  Counter()
w:  pest Counter({'p': 1, 'e': 1, 's': 1, 't': 1})
delta:  Counter()
w:  stew Counter({'s': 1, 't': 1, 'e': 1, 'w': 1})
delta:  Counter()
w:  show Counter({'s': 1, 'h': 1, 'o': 1, 'w': 1})
delta:  Counter()
filtered:  ['looks', 'pest', 'stew', 'show']
-----------------------------------
pc:  Counter({'a': 1, 'h': 1})
w:  suggest Counter({'s': 2, 'g': 2, 'u': 1, 'e': 1, 't': 1})
delta:  Counter({'a': 1, 'h': 1})
w:  letter Counter({'e': 2, 't': 2, 'l': 1, 'r': 1})
delta:  Counter({'a': 1, 'h': 1})
w:  of Counter({'o': 1, 'f': 1})
delta:  Counter({'a': 1, 'h': 1})
w:  husband Counter({'h': 1, 'u': 1, 's': 1, 'b': 1, 'a': 1, 'n': 1, 'd': 1})
delta:  Counter()
w:  easy Counter({'e': 1, 'a': 1, 's': 1, 'y': 1})
delta:  Counter({'h': 1})
w:  education Counter({'e': 1, 'd': 1, 'u': 1, 'c': 1, 'a': 1, 't': 1, 'i': 1, 'o': 1, 'n': 1})
delta:  Counter({'h': 1})
w:  drug Counter({'d': 1, 'r': 1, 'u': 1, 'g': 1})
delta:  Counter({'a': 1, 'h': 1})
w:  prevent Counter({'e': 2, 'p': 1, 'r': 1, 'v': 1, 'n': 1, 't': 1})
delta:  Counter({'a': 1, 'h': 1})
w:  writer Counter({'r': 2, 'w': 1, 'i': 1, 't': 1, 'e': 1})
delta:  Counter({'a': 1, 'h': 1})
w:  old Counter({'o': 1, 'l': 1, 'd': 1})
delta:  Counter({'a': 1, 'h': 1})
filtered:  ['husband']
-----------------------------------
pc:  Counter({'o': 1, 'g': 1, 'e': 1, 'u': 1})
w:  enough Counter({'e': 1, 'n': 1, 'o': 1, 'u': 1, 'g': 1, 'h': 1})
delta:  Counter()
w:  these Counter({'e': 2, 't': 1, 'h': 1, 's': 1})
delta:  Counter({'o': 1, 'g': 1, 'u': 1})
w:  play Counter({'p': 1, 'l': 1, 'a': 1, 'y': 1})
delta:  Counter({'o': 1, 'g': 1, 'e': 1, 'u': 1})
w:  wide Counter({'w': 1, 'i': 1, 'd': 1, 'e': 1})
delta:  Counter({'o': 1, 'g': 1, 'u': 1})
w:  wonder Counter({'w': 1, 'o': 1, 'n': 1, 'd': 1, 'e': 1, 'r': 1})
delta:  Counter({'g': 1, 'u': 1})
w:  box Counter({'b': 1, 'o': 1, 'x': 1})
delta:  Counter({'g': 1, 'e': 1, 'u': 1})
w:  arrive Counter({'r': 2, 'a': 1, 'i': 1, 'v': 1, 'e': 1})
delta:  Counter({'o': 1, 'g': 1, 'u': 1})
w:  money Counter({'m': 1, 'o': 1, 'n': 1, 'e': 1, 'y': 1})
delta:  Counter({'g': 1, 'u': 1})
w:  tax Counter({'t': 1, 'a': 1, 'x': 1})
delta:  Counter({'o': 1, 'g': 1, 'e': 1, 'u': 1})
w:  thus Counter({'t': 1, 'h': 1, 'u': 1, 's': 1})
delta:  Counter({'o': 1, 'g': 1, 'e': 1})
filtered:  ['enough']
-----------------------------------
pc:  Counter({'i': 1, 'm': 1, 's': 1, 'l': 1, 'p': 1, 'e': 1})
w:  claim Counter({'c': 1, 'l': 1, 'a': 1, 'i': 1, 'm': 1})
delta:  Counter({'s': 1, 'p': 1, 'e': 1})
w:  consumer Counter({'c': 1, 'o': 1, 'n': 1, 's': 1, 'u': 1, 'm': 1, 'e': 1, 'r': 1})
delta:  Counter({'i': 1, 'l': 1, 'p': 1})
w:  student Counter({'t': 2, 's': 1, 'u': 1, 'd': 1, 'e': 1, 'n': 1})
delta:  Counter({'i': 1, 'm': 1, 'l': 1, 'p': 1})
w:  camera Counter({'a': 2, 'c': 1, 'm': 1, 'e': 1, 'r': 1})
delta:  Counter({'i': 1, 's': 1, 'l': 1, 'p': 1})
w:  public Counter({'p': 1, 'u': 1, 'b': 1, 'l': 1, 'i': 1, 'c': 1})
delta:  Counter({'m': 1, 's': 1, 'e': 1})
w:  never Counter({'e': 2, 'n': 1, 'v': 1, 'r': 1})
delta:  Counter({'i': 1, 'm': 1, 's': 1, 'l': 1, 'p': 1})
w:  wonder Counter({'w': 1, 'o': 1, 'n': 1, 'd': 1, 'e': 1, 'r': 1})
delta:  Counter({'i': 1, 'm': 1, 's': 1, 'l': 1, 'p': 1})
w:  simple Counter({'s': 1, 'i': 1, 'm': 1, 'p': 1, 'l': 1, 'e': 1})
delta:  Counter()
w:  thought Counter({'t': 2, 'h': 2, 'o': 1, 'u': 1, 'g': 1})
delta:  Counter({'i': 1, 'm': 1, 's': 1, 'l': 1, 'p': 1, 'e': 1})
w:  use Counter({'u': 1, 's': 1, 'e': 1})
delta:  Counter({'i': 1, 'm': 1, 'l': 1, 'p': 1})
filtered:  ['simple']
'''


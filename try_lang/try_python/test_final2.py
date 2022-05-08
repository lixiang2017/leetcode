from typing import final

@final
class Leaf:
  print('Leaf')

class Other(Leaf):  # Error reported by type checker
  print('Other')



o = Other()


'''
$ python3 test_final2.py
Leaf
Other
'''
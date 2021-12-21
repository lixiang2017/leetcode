

'''
class TreeNodeold:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __add__(self, other):
        t = TreeNode()
        t.left = self
        t.right = other
        return t 
'''

class TreeNode:
    def __init__(self, pair=None):
        self.left = None
        self.right = None
        self.p = pair 
        # tree
        self.t, self.level = self.gen_tree(pair, 0)

    def __add__(self, other):
        t = TreeNode()
        t.left = self
        t.right = other.t 
        t.level = max(self.level, other.level) + 1
        if t.level > 4:
            t = self.explode(t)
        return t


    def gen_tree(self, pair, level):
        if not pair:
            return None, 0
        elif isinstance(pair, int):
            return pair, 1
        elif isinstance(pair[0], int) and isinstance(pair[1], int):
            self.left = pair[0]
            self.right = pair[1]
            self.level = 1 
            return self, 1 

        t = TreeNode()
        t.left, level1 = self.gen_tree(pair[0], level)
        t.right, level2 = self.gen_tree(pair[1], level)
        t.level = max(level1, level2) + 1
        return t

    def explode(self, t):

        return t 

    def split(self):
        pass


def get_magnitude(file_name):

    homework = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            homework.append(eval(line))

    print('homework: ', homework)

    sum_pair = TreeNode(homework[0])
    for i in range(1, len(homework)):
        sum_pair += TreeNode(homework[i])

    print('sum_pair: ', sum_pair)


    def myprint(pair):
        if not pair:
            return 
        elif isinstance(pair, int):
            print('int: ', pair)
            return 
        else:
            myprint(pair.left)
            myprint(pair.right)

    myprint(sum_pair)

    def get_mag(pair):
        if not pair:
            return 0
        elif isinstance(pair, int):
            return pair
        else:
            lm = get_mag(pair.left)
            # print('lm: ', lm)
            rm = get_mag(pair.right)
            # print('rm: ', rm)
            _sm = 3 * lm + 2 * rm
            print('lm, rm, sm: ', lm, rm, _sm)
            return _sm


    m = get_mag(sum_pair)
    print('m: ', m)


m1 = get_magnitude('input1')
m2 = get_magnitude('input2')
m3 = get_magnitude('input3')





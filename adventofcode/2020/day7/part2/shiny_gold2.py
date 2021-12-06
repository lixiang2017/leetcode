
from collections import defaultdict, deque
import re 
from pprint import pprint


def get_bags_count(file_name):
    # parent -> children count
    p2cs = defaultdict(dict)

    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # print('line: ', line)

            parent, children = line.split('contain')
            parent = parent.strip().replace('bags', '').replace('bag', '').strip()

            if 'no other' in children:
                p2cs[parent] = {}

            targets = re.findall(r'(\d+) ([a-z ]+)[^bag]', children)      
            if targets:
                for t in targets:
                    # print('t: ', t)
                    cnt, child = t
                    child = child.replace('bags', '').replace('bag', '').strip()
                    p2cs[parent][child] = int(cnt) 
    # print(p2cs)

    root = 'shiny gold'

    def get_color_cnt(color, color_cnt):
        if color not in p2cs:
            return 0
        if color in p2cs and not p2cs[color]:
            return 1 * color_cnt

        ans = color_cnt
        for child, child_cnt in p2cs[color].items():
            # print('child: ', child, child_cnt)
            ans += color_cnt * get_color_cnt(child, child_cnt)

        return ans

    root_cnt = get_color_cnt(root, 1) - 1
    print('root_cnt: ', root_cnt)
    return root_cnt


c1 = get_bags_count('input1')
c2 = get_bags_count('input2')
c = get_bags_count('input')

'''
('root_cnt: ', 32)
('root_cnt: ', 126)
('root_cnt: ', 5312)
'''



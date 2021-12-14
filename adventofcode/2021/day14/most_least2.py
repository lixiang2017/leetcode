



from collections import defaultdict, Counter

def get_diff(file_name, round):

    template = ''
    rules = defaultdict(str)
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            if '->' in line:
                left, right = line.split(' -> ')
                rules[left] = right 
            else:
                template = line

    init = list(template)
    n = len(init)
    for _ in range(round):
        now = []
        
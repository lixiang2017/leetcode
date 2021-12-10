




def get_score(file_name):
    score = 0
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    pair = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    stack = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            is_corrupted = False
            found = ''
            for ch in line:
                if ch in pair:
                    stack.append(ch)
                elif stack and pair[stack[-1]] == ch:
                    stack.pop()
                else:
                    # error
                    is_corrupted = True 
                    found = ch
                    break
            if is_corrupted and found:
                score += points[found]

    print('score: ', score)
    return score

c1 = get_score('input1')
c2 = get_score('input2')
c = get_score('input')


'''
score:  26397
score:  26397
score:  389589
'''




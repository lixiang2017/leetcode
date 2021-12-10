


def get_score(file_name):
    scores = []
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    pair = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    
    with open(file_name) as f:
        for line in f:
            stack = []
            line = line.strip()
            is_corrupted = False
            for ch in line:
                if ch in pair:
                    stack.append(ch)
                elif stack and pair[stack[-1]] == ch:
                    stack.pop()
                else:
                    # error
                    is_corrupted = True 
                    break
            if not is_corrupted:
                score = 0
                while stack:
                    score *= 5
                    score += points[pair[stack.pop()]]
                scores.append(score)
    scores.sort()
    print('scores: ', scores)
    mid = scores[len(scores) // 2]
    print('mid: ', mid)
    return mid

c1 = get_score('input1')
# c2 = get_score('input2')
c = get_score('input')


'''
scores:  [294, 5566, 288957, 995444, 1480781]
mid:  288957
scores:  [76873, 1327924, 12395921, 22412334, 26301796, 26765307, 26817499, 35054944, 77694624, 116132936, 119710842, 132182083, 132214817, 211670784, 221385334, 224349074, 319273592, 551739673, 578727422, 600680572, 609092281, 649811041, 730030812, 854636481, 1098695836, 1190420163, 1636477074, 3143348699, 3313201464, 4465738989, 5218462206, 5288769783, 5306068722, 5319286111, 5364395621, 5365726663, 5725930913, 6030779708, 8022545223, 11616200973, 12034118563, 16723260589, 17066322994, 17946068087, 18063801733, 20472536233, 21912633593, 26831560542, 26848582913, 27503879036, 28505807663]
mid:  1190420163
'''





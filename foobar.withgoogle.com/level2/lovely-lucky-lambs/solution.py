def solution(total_lambs):
    # Your code here
    # power of 2
    p, min1, p_total = 1, 0, 0
    while p_total + p <= total_lambs:
        p_total += p
        min1 += 1
        p *= 2
    
    fia, fib, max1, f_total = 1, 1, 0, 0
    if total_lambs <= 2:
        max1 = total_lambs
    else:
        max1 = f_total = 2
        fia, fib = fib, fia + fib
        while f_total + fib <= total_lambs:
            max1 += 1
            f_total += fib
            fia, fib = fib, fia + fib
    
    return max1 - min1
        
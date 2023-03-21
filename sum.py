def sum_range(begin, end, step = 1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum
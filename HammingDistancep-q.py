def HammingDistance(p, q):
    count = 0 
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count
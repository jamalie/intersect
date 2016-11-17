#intersect(s1, s2), where s1 and s2 are lists representing sets, computes and returns a list representing the intersection of the two sets. e.g.,

def intersect(s1, s2):
    newList = []

    for i in range(len(s1)):
        newList.append(cmp(s1[i],s2))

    return newList

def cmp(x,y):

    for i in range(len(y)):
        if x == y[i]:
            return x

print intersect([1, [2, 3], 4], [4, 2, [2, 3], 0])
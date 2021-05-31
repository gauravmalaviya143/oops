def topten():

    n = 1
    for x in range(n,6):
        sq = x*x
        yield sq

values = topten()
for i in values:
    print(i)
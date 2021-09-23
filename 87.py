def maxlist(l):
    large=l[0]
    for i in range(1,len(l)):
        if l[i] > large:
            large = l[i]
    return large
print(maxlist([1,2,5,7,8,9]))

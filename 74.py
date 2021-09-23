def maxlist(l):
    large =l[0]
    for i in range(len(l)-1):
        if(l[i] > l[i+1]):
            if(large<l[i]):
                large =l[i]
        else:
            if(large<l[i+1]):
                large = l[i+1]
    return large
print(maxlist([7,6,9,8,7,54,97,12,14]))
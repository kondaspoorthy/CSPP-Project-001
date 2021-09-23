def factors(n):
    factor=[ ]
    for num in range(1,n+1):
        if n % num==0:
            factor.append(num)
    return factor
print(factors(74))
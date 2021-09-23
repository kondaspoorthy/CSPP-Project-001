def getFirstName(text):
    k=text
    for i in range(len(k)):
        if(k[i]==' '):
            return k[:i]
print(getFirstName("Donald Knuth"))
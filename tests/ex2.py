def seperate(s):
	l = s.len()
	temp = s[0:l:4], s[1:l:2]
	return temp

print(seperate("a-c-e-g-i-")) 

# output: acegi-----

#Arithmeticoperators
c=2
d=5
print(c*d)
print(c%d)
print(c-d)
print(c+d)
print(c**d)
print(c//d)

#Assignmentoperators
e=7
e=e+7
print(e)
e+=5
print(e)
e-=3
print(e)

#Comparsionoperators
f=4
g=4

print(f==g)
print(f!=g)
print(f<=g)
print(f>=g)
print(f>g)
print(f<g)

#Logicaloperators
h=52

print(h<70 and h<100)
print(h>20 or h<1)
print (not h<70 and h<100)


#Membershipoperators

String1="Hello" 
print('H'in String1)

l=[10,20,30,40,50]
print(30 in l)

q=[20,60,40,80]
print(10 not in q)

#Identityoperators(similar to comparsion operator)
i=10
j=10

print(i is j)
print(i is not j)

#Bitwiseoperator
k=10
m=8

print(bin(k))       #binaryvalue for digit
print(bin(m))

print(k&m,bin(k&m))  
print(k|m,bin(k|m))

print(k^m,bin(k^m))

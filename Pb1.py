import math

num = range(1,1000)
num[-1]

Somme_multiples =  0
for i in num :
    if i % 3 ==0 or i % 5  == 0 :
        Somme_multiples = i + Somme_multiples

print(Somme_multiples)
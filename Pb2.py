reponse = 0
i = 1
j = 2
while i <= 4000000:
    if i % 2 == 0:
        reponse += i
    i, j = j, i + j
print(reponse)
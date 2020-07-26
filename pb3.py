from math import floor

def facteur(num):
    result = []
    if num == 2:
        result.append(2)
        return result
    for i in range(3, int(floor(num ** 0.5)), 2):
        if num % i == 0 :
            if len(facteur(i)) == 0 :
                result.append(i)
    return result
print(facteur(600851475143))


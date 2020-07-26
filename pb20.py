from math import factorial

def main(num=100):
    fact = factorial(num)
    list1 = [int(x) for x in str(fact)]
    return sum(list1)
print(main())
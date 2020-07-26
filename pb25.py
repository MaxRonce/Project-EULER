def fib(num):
    a, b = 1, 1
    fibo = [1, 1]
    for i in range(0, num):
        c = a+b
        fibo.append(c)
        a = b
        b = c
    return fibo





if __name__ == "__main__":
    fibo = fib(1000)
    i = 0
    while len(str(fibo[i])) < 1000 :
        i +=1
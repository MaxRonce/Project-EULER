def main():
    max = 1000
    for a in range(1, max+1) :
        for b in range(a +1, max + 1):
            c = max - a - b
            if a*a + b*b == c*c :
                return a*b*c

if __name__ in "__main__":
    print(main())
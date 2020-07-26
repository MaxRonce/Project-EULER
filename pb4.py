def est_palindrome():
    reponse = max(i*j
        for i in range(10,1000)
        for j in range(10,1000)
        if str(i*j) == str(i*j)[::-1])
    return str(reponse)

if __name__ == "__main__":
    print(est_palindrome())
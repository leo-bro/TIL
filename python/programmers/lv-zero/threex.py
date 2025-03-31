def threex(n):
    if n == 1:
        return 1
    num = threex(n - 1) + 1
    while True:
        if (num % 3 == 0) or any(digit in str(num) for digit in "3"):
            num += 1
        else:
            break
    return num


for i in range(1, 100):
    print(threex(i))

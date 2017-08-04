n = int(input())
for i in range(0, n+1):
    msg = ''
    if (i % 5 == 0):
        msg += "fizz"
    if (i % 3 == 0):
        msg += "buzz"
    print(msg or i)

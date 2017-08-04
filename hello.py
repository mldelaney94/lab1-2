print("Hello World")
n = int(input())
def fizz_buzz (n):
    for i in range (0, n+1): #displays up to number entered
        msg = ''
        if i % 3 == 0:
            msg += "Fizz"
        if i % 5 == 0:
            msg += "Buzz"
        print (msg or i)

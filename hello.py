print("Hello World")
def fizz_buzz ():
    for i in range (0, 101): #displays upto 100
        msg = ''
        if i % 3 == 0:
            msg += "Fizz"
        if i % 5 == 0:
            msg += "Buzz"
        print (msg or i)

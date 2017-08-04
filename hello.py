print("Hello World")
def fizz_buzz ():
    for i in range (0, 100): #displays up to number entered
        msg = ''
        if i % 3 == 0:
            msg += "Fizz"
        if i % 5 == 0:
            msg += "Buzz"
        print (msg or i)

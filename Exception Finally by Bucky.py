'''
THIS IS BUCKY 'Exception' and 'Finally' EXAMPLES 
'''



while True:
    try:
        num = int(input("Enter a number: \n"))  # When the value entered is Int, it will print and exit loop
        print(10/num)
        break
    except ValueError:
        print("Enter only integers")  # only when the value enter is not integer
    except ZeroDivisionError:
        print("Don't enter zero")  # only when the is divide-by-Zero case
    finally:
        print("Loop number: ")  # this line of Finally will ALWAYS b printed in every loop


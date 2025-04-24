try:
    num1=int(input("enter the number"))
    num2=int(input("enter the number"))
    result=num1/num2
    print(result)
    print(result1)

except ZeroDivisionError :
    print("division with 0 is not possible")
except ValueError:
    print("thier is a error in the value")
except NameError:
    print("error in the name ")
except :
    print("some other error")
finally:
    print("no matter what happens")
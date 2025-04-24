try:
    num=int(input("enter the number"))
    print(num)
except ValueError as er:
    print(er)

print("i am outside the try block")
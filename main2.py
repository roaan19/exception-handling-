valid=False
while not valid:
  try:
    num=int(input("enter the number"))
    while num%2==0:
        print("messi")
        valid=True
  except ValueError:
     print("their is error in the value ")
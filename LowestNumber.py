print("Give 3 random numbers!")
print("I'll tell you which number is the lowest.")

First = int(input("FirstNumber: "))
Second = int(input("SecondNumber: "))
Third = int(input("ThirdNumber: "))

if First < Second and First < Third:
    print(f"The lowest number is {First}")
else:
    if Second < First and Second < Third:
        print(f"The lowest number is {Second}")
    else:
        if Third < First and Third < Second:
            print(f"The lowest number is {Third}")
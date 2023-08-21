#prompt user for value

def prompt_menu():
    a = float(input("please enter first number: "))
    b = float(input("and the second number: "))
    print("""
Chose you operation:
1 = sum
2 = difference
3 = multiplication
4 = division
5 = power
""")
    op = (int(input("enter your mathmatical function choice: ")))
    return a ,b ,op

#perform operations

def calculate():
    a, b, op = prompt_menu()       
    if op == 1:
        print("sum: {} + {} = {}".format(a,b,a+b))

    elif op == 2:
        print("difference: {} - {} = {}".format(a,b,a-b))

    elif op == 3:
        print("multiplication: {} * {} = {}".format(a,b,a*b))

    elif op == 4:    
        print("division: {} / {} = {}".format(a,b,a/b))

    elif op == 5:
        print("power: {} ^ {} = {}".format(a,b,a**b))

    else:
        print("No such choice!")
    loop()

def loop():
    choice = input("Do you want to carry out another calculation (Y/N): ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print("Goodbye")
    else:
        print("Not valid entry!")
        loop()      

calculate()

def ask_user():
    print ()
    try:
        x = int(input("please enter a range for generating random numbers"))
    except:
        Print("Please enter a valid integer")

    y = random_gen(x)
    print(y)
    
def random_gen(a):
    import random
    for i in range (a):
        x = random.random()
        print (x)
    return "Hoohah"

ask_user()



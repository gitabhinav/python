l_option = int(input("Is temperature in C (1) or F(2)"))

if l_option != 1 and l_option != 2 :
    print("Invalid option")
else:
    l_temp = float(input("Enter the temperature"))
    if l_option == 1:
        #logic for C
        print("The temperature in F is:", (((l_temp*9)/5)+32))
    else:
        #logic for F
        print("The temperature in C is: ", (((l_temp -32)*5)/9))


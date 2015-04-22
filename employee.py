try:
    emp_hrs = int(input("Enter working hours"))
    rate = int(input("Enter hourly rate"))
    if emp_hrs > 40:
               pay = ((emp_hrs -40)*1.5*rate )+ 40 *rate
    else:
               pay = emp_hrs *rate

    print("Pay:", pay)
        

except:
    print("please enter valid number")

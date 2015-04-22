def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

count = 0
total = 0
while True:
    data = input("Enter a number:")
    if is_number(data):
        count = count + 1
        total = total + float(data)
    elif data.upper() == "DONE":
        print ("Count:", count)
        print ("Total:", total)
        try:
            avg = total/count
        except:
            avg = 0
            
        print ("Average:",avg )
        break
    else:
        print("Please enter a valid number")
        
        
        

#Exercise 3.2: Rewrite your pay program using try and except so 
# that yourprogram handles non-numeric input gracefully by 
# printing a messageand exiting the program. The following 
# shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

hrs = input("Enter Hours: ")

try:
    h = float(hrs)
    rph = input("Enter Rate: ")
    try:
        r = float(rph)
        if h <= 40:
            pay = h * r
    
        else:
            overhours = h - 40
            norm_pay = 40 * r
            over_pay = overhours * r * 1.5
            pay = norm_pay + over_pay

        print(pay)

    except:
        print("Error, please enter numeric input")
except:
    print("Error, please enter numeric input")
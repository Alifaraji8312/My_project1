number1=input("please enter the first numbers:")
if not number1.replace('.','',1).isdigit():
    print("error:please enter only numbers.")
    exit()
number1=float(number1)
operator=input("please enter the operator(+,-,*,/):")
number2=input("please enter the second numbers:")
if not number2.replace('.','',1).isdigit():
    print("errer:please enter only numbers.")
    exit()
number2=float(number2)
if operator =="+":
    result=number1+number2
elif operator =="-":
    result=number1-number2
elif operator =="*":
    result=number1*number2
elif operator =="/":
    if number2 !=0:
        result=number1/number2
    else:
        result="errer:divide by zero."
else:
    result="lnvalid operator."                          
   
print(f"the result:{result}")         
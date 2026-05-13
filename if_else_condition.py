#if condition
age = 17
if age >= 18:
    print("You are Eligible to vote")

#If Else

num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#ElseIf
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#Nested IF

age = 15
nationality = "China"
if age >= 18:
    if nationality == "India":
        print("You are Eligible to vote")
    else:
        print("You are not Eligible to vote")
else:
    print("You are Under Age")
#Banking Example
#Intial Balance
acc_holder_name = "Preetti"
balance = 5000
atm_pin = 1234

#User Input
print("Welcome to ABC Bank")

entered_pin = int(input("Enter the pin number: "))
if entered_pin == atm_pin:
    print("You can withdraw")
else:
    print("You can not withdraw")

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


# If elseIf
#Intial Balance
acc_holder_name = "Preetti"
balance = 5000
atm_pin = 1234

#User Input
print("Welcome to ABC Bank")

entered_pin = int(input("Enter the pin number: "))

#Pin Verification
if entered_pin == atm_pin:
    print("Pin Verified Successfully")
    print("Available balance is:", balance)

withdraw_amount = int(input("Enter the withdraw amount: "))
if withdraw_amount <= balance:
    if withdraw_amount % 100 == 0:
        balance = balance - withdraw_amount
        print("Please collect your cash")
        print("Withdrwal Successful")
        print("Your Available balance is:", balance)
    else:
        print("Amount should be multiple of 100")
else:
    print("You don't have enough cash")


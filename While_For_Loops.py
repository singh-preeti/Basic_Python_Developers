
#For Loop
# Fixed number of iteration
days = [1,2,3,4,5,6,7,8,9,10,11,12]
fruits = ["apple","banana","orange","strawberry"]
for i in fruits:
    print(i)
#While Loop
# until the condition is true , number or of iteration is not fixed


balance = 5000

while True:
    amount = int(input("Enter amount: "))

    if amount <= balance:
        balance -= amount
        print("Remaining balance:", balance)
    else:
        print("You don't have enough money")

    # stop when balance becomes 0
    if balance == 0:
        print("Balance is empty")
        break

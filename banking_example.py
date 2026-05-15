#Banking Example with operators,while loop,condition and match case

acc_holder_name = "Preetti"
balance = 1000

while True:

    print("----Bank Menu-----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Current Balance: ", balance)

        case 2:
            deposit = int(input("Enter your amount: "))
            balance =  balance + deposit
            print("Money deposited: ", deposit)
            print("Current Balance: ", balance)

        case 3:
            withdraw = int(input("Enter your amount: "))

            if balance >= withdraw:
                balance = balance - withdraw
                print("Money withdraled: ", withdraw)
            else:
                print("Insufficient Balance .")

        case 4:
                print("Thank you for Banking!")
                break


        case _:
            print("Invalid choice")

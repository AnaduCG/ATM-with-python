
acc_names = ('John', 'James', 'Emeka')

acc_details = {
    'James': ['123', '100'],
    'John': ['1234', '200'],
    'Emeka': ['12345', '10'],
}


u_name = input("Enter your acc name ")


def begin():
    if u_name in acc_names:

        atm_pin = input(f"Welcome {u_name} plaese enter your atm pin ")
        if atm_pin == (acc_details[u_name][0]):
            while atm_pin == (acc_details[u_name][0]):
                options = input(f"""{u_name} what would you like to do
                1 to check  ballance
                2 to deposite
                3 to withdraw
                0 to exit
                """)
                if options == '1':
                    check_balance()
                elif options == '2':
                    deposite()
                elif options == '3':
                    withdrawal()
                elif options == '0':
                    print(f"Bye {u_name} thanks for banking with us")
                    break
            else:
                print("wrong pin")
    else:
            print("name does not exist in our database")


def withdrawal():
    withdrawal_amount = float(input("Enter withdrawal amount "))
    if withdrawal_amount < float(acc_details[u_name][1]):
        new_bal = float(acc_details[u_name][1]) - withdrawal_amount
        print(
            f"Withdrawal of {withdrawal_amount}$ was successful, your new ballance is {new_bal}$")
    else:
        print("insuficient ballance")


def deposite():
    deposite_amount = float(input("Enter deposite amount "))
    new_bal = deposite_amount + float(acc_details[u_name][1])
    print(
        f"You have successfuly deposited {deposite_amount}$ and your new ballance is {new_bal}$")


def check_balance():
    print(f"Dear {u_name} your account ballance is {acc_details[u_name][1]}$")


# print( type(int(acc_details['James'][0])))
begin()
# print( acc_details['Emeka'][1])

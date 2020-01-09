total=0
print('Welcome to the ATM!')
print('How can we help you today?')
print('1. Withdraw')
print('2. Deposit')
print('3. Check Balance')
print('4. Quit')
while True:
    trans=int(input('Choose an option'))
    if trans==1:
        print('How much do you want to withdraw?')
        withdraw=int(input('Choose an ammount'))
        if total-withdraw<0:
            print('We are sorry, but there is an error')
        elif withdraw>=0:
            print(f'You have withdrawn ${withdraw}') 
            total=total-withdraw
            print(f'Your total account balance is ${total}')
        else:
            print('We are sorry, but there is an error')
    elif trans==2:
        print('How much do you want to deposit')
        deposit=int(input('Choose an ammount'))
        if deposit>=0:
            print(f'You have deposited ${deposit}')
            total=total+deposit
            print(f'Your total account balance is ${total}')
        else:
            print('We are sorry, but there is an error')
    elif trans==3:
        print(f'You have a balance of ${total}')
    elif trans==4:
        break
    else:
        print('We are sorry, but there is an error')
print('Have a nice day!')
# create a restaurant bill calculator that generates a total amount between 1000 and 3000. and also asks the number of guests per table.
# this also takes in the % of total amount of tip that user wants wants to spend
# output should provide number that each guest is paying including tips or total amount plus tip for a in a single payment

#importing random
import random

total_price = random.randint(100, 300)

# creating welcome format
line = '-'*80
w_string = "Ade's bill service"

WELCOME = '\n' + line + '\n' + w_string + '\n' + line + '\n'
print (WELCOME)

# creating menu display
print(f'Here is your bill\n')
print(f'You have spent a total of £{total_price}')
MENU = (f'How would you like top pay this bill?\n'
        f'\nPress 1 to split the bill\n'
        f'Press 2 to make to a single payment\n'
        f'Enter 3 to quit program')

# constant percentages
percent10 = ((10/100)*total_price) 
percent15 = ((15/100)*total_price) 
percent20 = ((20/100)*total_price) 
# code start
while True:
    print(MENU)
    payment_answer = input('')
    # splitting the bill option
    if payment_answer == '1':
        split_type =input(f'How do you want to split the bill\n'
                       f'Press 1 to split evenly amongst all guests\n'
                       f'Press 2 to split amongst only a number of guests\n')
        # splitting evenly
        if split_type == '1':
            no_of_guests = int(input(f'How many guests are on this table?'))
            tip_answer = input(f'Your total bill is £{total_price}. Would you like to leave a tip?\n'
                               f'Please answer yes or no: ')
            # tipping answer
            if tip_answer.lower() == 'yes' :
                tip_type= input(f'Do you want to leave a specific amount or do you want to leave a percentage of the final bill\n'
                                f'Press 1 for percentage\n'
                                f'Press 2 for specific amount\n')
                # percentage pay
                if tip_type == '1':
                    tip_percent = input(f'What percentage of the bill would you like to tip?\n'
                                        f'Here are some examples\n'
                                        f'10% = {percent10}\n'
                                        f'15% = {percent15}\n'
                                        f'20% = {percent20}\n')
                    try: #exception handling
                        tip_percent = int(tip_percent)
                        tip_amount = (tip_percent/100)*total_amount  
                        total_amount = tip_amount + total_price
                        price_per_guest1 = total_amount/no_of_guests
                        print (f'Your final bill is £{total_amount}\n'
                            f'Each guest has to pay £{price_per_guest1}\n'
                            f'Thank you for visiting. See you again!')
                    except ValueError: #exception handling
                        print('Please enter a valid number')
                    # specific payment amount
                elif tip_type == '2':
                    tip_spec_amount = input('How much would you like to pay?\n')
                    try: #exception handling
                        total_amount_spec = int(tip_spec_amount) + total_price
                        price_per_guest2 = total_amount_spec/no_of_guests
                        print (f'Your final bill is £{total_amount_spec}\n'
                            f'Each user has to pay £{price_per_guest2}\n'
                            f'Thank you for visiting. See you again')
                    except ValueError:
                        print('Please enter a valid number')
                    # no tipping
            elif tip_answer.lower() == 'no':
                price_per_guest3 = total_price/no_of_guests
                print(f'Your total bill is {total_price}\n'
                      f'Each guest has to pay {price_per_guest3}'
                      f'Thank you for not leaving a tip')
        # splitting among custom number of people        
        elif split_type == '2':
            number_to_split  = int(input('How many people do you want to split among?: '))
            split_type_custom_guest = input(f'Would you like to leave a tip?\n'
                                            f'Answer yes or no\n')
            # splitting among custom number of people and tipping
            if split_type_custom_guest.lower() == 'yes':
                tip_type= input(f'Do you want to leave a specific amount or do you want to leave a percentage of the final bill\n'
                                f'Press 1 for percentage\n'
                                f'Press 2 for specific amount\n')
                # percentage tipping
                if tip_type == '1':
                    tip_percent = input(f'What percentage of the bill would you like to tip?\n'
                                        f'Here are some examples\n'
                                        f'10% = {percent10}\n'
                                        f'15% = {percent15}\n'
                                        f'20% = {percent20}\n')
                    tip_percent = int(tip_percent)
                    tip_amount = tip_percent/100*(total_price)
                    total_amount = tip_amount + total_price
                    price_per_guest1 = total_amount/number_to_split
                    print (f'Your final bill is £{total_amount}\n'
                           f'Each guest has to pay £{price_per_guest1}\n'
                           f'Thank you for visiting. See you again!')
                    # custom tipping
                elif tip_type == '2':
                    tip_spec_amount = input('How much would you like to pay?\n')
                    total_amount_spec = (int(tip_spec_amount) + total_price)
                    price_per_guest2 = total_amount_spec/number_to_split
                    print (f'Your final bill is £{total_amount_spec}\n'
                           f'Each user has to pay £{price_per_guest2}\n'
                           f'Thank you for visiting. See you again')
                    # no tipping among guest
            elif split_type_custom_guest.lower() == 'no':
                price_per_guest3 = total_price/number_to_split
                print(f'Your total bill is {total_price}\n'
                      f'Each guest has to pay {price_per_guest3}'
                      f'Thank you for not leaving a tip ')
        else:
            print('Invalid answer, Try again')
            # single payment code
    elif payment_answer == '2': 
        single_payment = input(f'Your total bill is {total_price}\n'
                               f'Would you like to leave a tip?\n')
        # single payment tip 
        if single_payment.lower() == 'yes' :
            tip_type= input(f'Do you want to leave a specific amount or do you want to leave a percentage of the final bill\n'
                                f'Press 1 for percentage\n'
                                f'Press 2 for specific amount\n')
            if tip_type == '1':
                tip_percent =input(f'What percentage of the bill would you like to tip?\n'
                                    f'Here are some examples\n'
                                    f'10% = {percent10}\n'
                                    f'15% = {percent15}\n'
                                    f'20% = {percent20}\n')
                tip_percent =  int(tip_percent)
                tip_amount = tip_percent/100*total_price  
                total_amount = tip_amount + total_price
                print (f'Your final bill is £{total_amount}\n'
                       f'Thank you for visiting. See you again!')
            elif tip_type == '2':
                tip_spec_amount = input('How much would you like to pay?\n')
                total_amount_spec = (int(tip_spec_amount) + total_price)
                print (f'Your final bill is £{total_amount_spec}\n'
                       f'Thank you for visiting. See you again')
        elif single_payment.lower() == 'no':
            print(f'Your total bill is {total_price}\n'
                  f'Thank you for not leaving a tip')
        else:
            print('Invalid answer, Try again')
    # breaking from loop
    elif payment_answer =='3':
        print('Goodbye!')
        break

    # invaid answer
    else:
        print('Invalid answer, Try again')



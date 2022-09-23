# importing required libraries
import random
import json
import os

# defining the default values
number_of_days = 0
money = 1000
stock_value = random.randint(199, 1001)
day_counter = 0
number_of_shares = 0


def tips():
    with open('tips.json') as fp:
        data = json.load(fp)
        tips_from_data = data['tips']
        random_tips = random.choice(tips_from_data)
        quote = random_tips['quotes']
        author = random_tips['author']

        return f'{quote}\n- {author}'


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def display():
    global money
    global stock_value
    global number_of_shares
    global day_counter

    if money >= 1000000000000:
        TIP = 'VERY VERY Impressive!!! Now just do that in the real world and you will be set for life'
    elif money >= 1000000000:
        TIP = 'Can you teach me your ways? Because that was amazing!'
    elif money >= 1000000:
        TIP = 'WOW WOW WOW, very good indeed.'
    elif money <= 10:
        TIP = 'YOU LOST THE MONEY!!! oh well.. back to McDonald\'s I guess'
    else:
        TIP = tips()

    cls()
    print(f'''
    Day: {number_of_days}
    Money: ${money}
    Stock Price: ${stock_value}
    Number of Shares: {number_of_shares}
    Number of Days left: {day_counter}
    ''')
    print(TIP)


def buy():
    global money
    global stock_value
    global number_of_shares
    global day_counter

    if money > 0:
        number_of_shares += 1
        money -= stock_value
        day_counter -= 1
        print(f'You bought 1 share for ${stock_value}')
        print(f'You have ${money} left')
        print(f'You have {number_of_shares} shares')
    else:
        print('You do not have enough money to buy a share')


def sell():
    global money
    global stock_value
    global number_of_shares
    global day_counter

    if number_of_shares > 0:
        number_of_shares -= 1
        money += stock_value
        day_counter -= 1
        print(f'You sold 1 share for ${stock_value}')
        print(f'You have ${money} left')
        print(f'You have {number_of_shares} shares')
    else:
        print('You do not have any shares to sell')


def wait():
    global day_counter
    day_counter -= 1
    print('You waited a day')


def end():
    global money
    global number_of_shares
    global stock_value
    global day_counter
    global number_of_days

    if number_of_shares > 0:
        money += stock_value * number_of_shares
        print(f'You sold {number_of_shares} shares for ${stock_value * number_of_shares}')
    print(f'You have ${money} left')
    print(f'You have {number_of_shares} shares')
    print(f'You have played {number_of_days - day_counter} days')
    print('Thank you for playing!')
    exit()


def game():
    global money
    global stock_value
    global number_of_shares
    global day_counter
    global number_of_days

    number_of_days = int(input('How many days would you like to play for? '))
    day_counter = number_of_days
    while day_counter > 0:
        display()
        choice = input('What would you like to do? \n Buy || Sell || Wait || End\n').lower()
        if choice == 'buy':
            buy()
        elif choice == 'sell':
            sell()
        elif choice == 'wait':
            wait()
        elif choice == 'end':
            end()
        else:
            print('Invalid input')
        stock_value = random.randint(199, 1001)
        day_counter -= 1
    end()


if __name__ == '__main__':
    game()

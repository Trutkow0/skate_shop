# Timothy Rutkowski 05/052024 timothyRutkowski_finalExam.py

# Constants = MACRO_CASE
# Functions = camelCase
# Variables = snake_case

# This program will have two features.
# The first feature will calculate the cost of skates for a customer at the 
# CPCC Skate Shop. Total pricing will include the tyoe of skate, the number of 
# skates, and a 7.25% sales tax.

# The second feature will randomly generate the amount of roller skates or
# roller blades being purchased and add a discount to the purchase based on the
# day of the week.

import random

# Constants
SALES_TAX = 0.0725
ROLLER_SKATES_MIN = 155.00 # price for min number of roller skates purchased (1-2 pairs)
ROLLER_SKATES_MAX = 142.50 # price for max number of roller skates purchased (3+ pairs)
ROLLER_BLADES_MIN = 219.95 # price for min number of roller blades purchased (1-2 pairs)
ROLLER_BLADES_MAX = 189.95 # price for max number of roller blades purchased (3+ pairs)
# Daily Discounts
M_T_DISCOUNT = 0.035 # Discount for Monday and Tuesday
W_H_DISCOUNT = 0.0325 # Discount for Wednesday and Thursday
F_S_DISCOUNT = 0.03 # Discount for Friday and Saturday
U_DISCOUNT = 0.045 # Discount for Sunday

# Functions
# Main function of the program
def main():
    print('Choose from one of the following program options:'
          '\n\t1. Process Single Order'
          '\n\t2. Generate Random Number Of Skates With Discounts')
    program_option = input('Which program will run? ')
    if program_option == '1':
        processSingleOrder()
    elif program_option == '2':
        generateRandomSkatesWithDiscount()
    else:
        print("Invalid option. Please enter '1' or '2'.")




# Function to process a single order        
def processSingleOrder():
    displayMainMenu()
    skates_option = selectSkateType()
    num_pairs, price_per_pair = selectAmount(skates_option)
    subtotal, sales_tax, total = calcPrice(num_pairs, price_per_pair)
    displaySingleOrderResults(subtotal, sales_tax, total)
    
# Function to generate random skates with discount
def generateRandomSkatesWithDiscount():
    displayMainMenu()
    skates_option = selectSkateType()
    num_pairs = generateRandomNum()
    price_per_pair = getPricePerPair(skates_option, num_pairs)
    displayWeek()
    day_of_week = chooseDayOfWeek()
    discount = getDiscount(day_of_week)
    subtotal, sales_tax, discount_amount, total = calcDiscount(num_pairs, price_per_pair, discount)
    displayDiscountResults(skates_option, num_pairs, subtotal, sales_tax, discount_amount, total)




# Function to display the main menu
def displayMainMenu():
    print('**Welcome to the CPCC Skate Shop**')
    print('Choose from one of the following types of skates:' +
          '\n\t1. Roller Skates' +
          '\n\t2. Roller Blades')

# Function for user to choose the type of skates being purchased
def selectSkateType():
    while True:
        try:
            skates_option = input('Which type of skates will be purchased? ')
            if skates_option not in ('1', '2'):
                raise ValueError("Please choose '1' for Roller Skates or '2' "
                                 "for Roller Blades.")
            return skates_option
        except ValueError as e:
            print(f"\tInvalid Input: {e}")        
            
# Function for the user to select the number of pairs of skates being purchased
# and get the price per pair.
def selectAmount(skates_option):
    while True:
        try:
            if skates_option == '1':
                num_pairs = int(input('\nHow many roller skates will be '
                                      'purchased? '))
                price_per_pair = ROLLER_SKATES_MIN if num_pairs in range(1, 3) else ROLLER_SKATES_MAX
            else:
                num_pairs = int(input('\nHow many roller blades will be '
                                      'purchased? '))
                price_per_pair = ROLLER_BLADES_MIN if num_pairs in range(1, 3) else ROLLER_BLADES_MAX
            return num_pairs, price_per_pair
        except ValueError as e:
            print(f'\tInvalid Input: Please enter a valid numerical '
                  'value. (Ex: 2)')    

# Function to calculate the price of purchase
def calcPrice(num_pairs, price_per_pair):
    subtotal = num_pairs * price_per_pair
    sales_tax = SALES_TAX * subtotal
    total = subtotal + sales_tax
    return subtotal, sales_tax, total

# Function to display the results of the purchase
def displaySingleOrderResults(subtotal, sales_tax, total):
    print(f'\tSubtotal: ${subtotal:.2f}')
    print(f'\tSales Tax: ${sales_tax:.2f}')
    print(f'\nThe total cost of this purchase ${total:.2f}')




# Functions for randomly generating number of skates and applying a discount
# depending on the day of the week
# Function to randomly generate the number of skates being purchased
def generateRandomNum():
    num_pairs = random.randint(1, 101)
    return num_pairs

# Function to display valid options for the day of the week    
def displayWeek():
    print('Choose from a day of the week to recieve a discount:')
    print('\tM - Monday')
    print('\n\tT - Tuesday')
    print('\n\tW - Wednesday')
    print('\n\tR - Thursday')
    print('\n\tF - Friday')
    print('\n\tS - Saturday')
    print('\n\tU - Sunday')

# Function for the user to select the day of the week    
def chooseDayOfWeek():
    while True:
        day_of_week = input('What day of the week is it?: ').upper()
        if day_of_week in ['M', 'T', 'W', 'R', 'F', 'S', 'U']:
            return day_of_week
        else:
            print('Invalid Input. Please enter one of the options listed.')
            
# Function to get the discount depending on the day of the week as entered by
# the user
def getDiscount(day_of_week):
    if day_of_week in ['M', 'T']:
        return M_T_DISCOUNT
    elif day_of_week in ['W', 'R']:
        return W_H_DISCOUNT
    elif day_of_week in ['F', 'S']:
        return F_S_DISCOUNT
    elif day_of_week == 'U':
        return U_DISCOUNT

# Function to get the price per pair of skates depending on user selection
def getPricePerPair(skates_option, num_pairs):
    if skates_option == '1':
        price_per_pair = ROLLER_SKATES_MIN if num_pairs in range(1, 3) else ROLLER_SKATES_MAX
        return price_per_pair
    elif skates_option == '2':
        price_per_pair = ROLLER_BLADES_MIN if num_pairs in range(1, 3) else ROLLER_BLADES_MAX
        return price_per_pair
    else:
        raise ValueError("Invalid skates option.")    

# Function to calculate results with the discount added
def calcDiscount(num_pairs, price_per_pair, discount):
    subtotal = num_pairs * price_per_pair
    discount_amount = discount * subtotal
    total_discounted = subtotal - discount_amount
    sales_tax = SALES_TAX * total_discounted
    total = total_discounted + sales_tax
    return subtotal, sales_tax, discount_amount, total

# Funtion to display results with the discount added    
def displayDiscountResults(skates_option, num_pairs, subtotal, sales_tax, discount_amount, total):
    if skates_option == '1':
        print(f'\nNumber of roller skates purchased: {num_pairs}')
    else:
        print(f'\nNumber of roller blades purchased: {num_pairs}')
    print(f'\tSubtotal: ${subtotal:.2f}')
    print(f'\tSales Tax: ${sales_tax:.2f}')
    print(f'\tDiscount: ${discount_amount:.2f}')
    print(f'\nThe final cost of this purchase ${total:.2f}')    


if __name__ == '__main__':
    main()
if __name__ == '__main__':
    orders = {
        'wings': 0,
        'cookies': 0,
        'spring rolls': 0,
        'salmon': 0,
        'steak': 0,
        'meat tornado': 0,
        'a literal garden': 0,
        'ice cream': 0,
        'cake': 0,
        'pie': 0,
        'coffee': 0,
        'tea': 0,
        'blood of the innocent': 0,
    }
    print(
        '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Blood of the Innocent
        '''
    )
    while True:
        print(
            '''
***********************************
** What would you like to order? **
***********************************
            '''
        )
        user_input = input('>   ')
        if user_input == 'quit':
            break
        if user_input.lower() in orders.keys():
            orders[user_input.lower()] += 1
            print('\n** {1} order of {0} have been added to your meal **'.format(user_input, orders[user_input.lower()]))
        else:
            print('\nSorry we don\'t carry', user_input)
if __name__ == '__main__':
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
        print('\n** Your order of {0} have been added to your meal **'.format(user_input))
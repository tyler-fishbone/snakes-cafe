
menu = {
        'wings': {
            'category': 'appetizers',
            'orders': 0,
        },
        'cookies': {
            'category': 'appetizers',
            'orders': 0,
        },
        'spring rolls': {
            'category': 'appetizers',
            'orders': 0,
        },
        'brussel sprouts': {
            'category': 'appetizers',
            'orders': 0,
        },
        'brains': {
            'category': 'appetizers',
            'orders': 0,
        },
        '6 compliments': {
            'category': 'appetizers',
            'orders': 0,
        },
        'salmon': {
            'category': 'entrees',
            'orders': 0,
        },
        'steak': {
            'category': 'entrees',
            'orders': 0,
        },
        'meat tornado': {
            'category': 'entrees',
            'orders': 0,
        },
        'a literal garden': {
            'category': 'entrees',
            'orders': 0,
        },
        'cheeseburger': {
            'category': 'entrees',
            'orders': 0,
        },
        'lasagne': {
            'category': 'entrees',
            'orders': 0,
        },
        'cottage cheese': {
            'category': 'sides',
            'orders': 0,
        },
        'apple sauce': {
            'category': 'sides',
            'orders': 0,
        },
        'over-ripe banana': {
            'category': 'sides',
            'orders': 0,
        },
        'freedom fries': {
            'category': 'sides',
            'orders': 0,
        },
        'pickle': {
            'category': 'sides',
            'orders': 0,
        },
        'cabbage': {
            'category': 'sides',
            'orders': 0,
        },
        'ice cream': {
            'category': 'desserts',
            'orders': 0,
        },
        'cake': {
            'category': 'desserts',
            'orders': 0,
        },
        'pie': {
            'category': 'desserts',
            'orders': 0,
        },
        'chocolate spaghetti': {
            'category': 'desserts',
            'orders': 0,
        },
        'foot massage': {
            'category': 'desserts',
            'orders': 0,
        },
        'coconut ice cream': {
            'category': 'desserts',
            'orders': 0,
        },
        'coffee': {
            'category': 'drinks',
            'orders': 0,
        },
        'tea': {
            'category': 'drinks',
            'orders': 0,
        },
        'blood of the innocent': {
            'category': 'drinks',
            'orders': 0,
        },
        'carp saliva': {
            'category': 'drinks',
            'orders': 0,
        },
        'bacardi 151': {
            'category': 'drinks',
            'orders': 0,
        },
        'code fellows tap water': {
            'category': 'drinks',
            'orders': 0,
        },
    }


def main():
    print_header()
    print_appetizers()
    print_entrees()
    print_desserts()
    print_drinks()
    user_prompt()


def print_header():
    print(
        '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
        '''
    )


def get_menu_items_from_category(category):
    menu_item_list = []
    if type(category) is not str:
        raise TypeError('Argument invalid. Must be string.')
    if category not in [data['category'] for data in menu.values()]:
        raise LookupError('Argument invalid. Must be valid category from menu dict.')
    for key, value in menu.items():
        if value['category'] == category:
            menu_item_list.append(key)
    return menu_item_list


def print_appetizers():
    print(
        '''
Appetizers
----------'''
    )
    menu_list = get_menu_items_from_category('appetizers')
    for item in menu_list:
        print(item)


def print_entrees():
    print(
        '''
Entrees
-------'''
    )
    menu_list = get_menu_items_from_category('entrees')
    for item in menu_list:
        print(item)


def print_desserts():
    print(
        '''
Desserts
-------'''
    )
    menu_list = get_menu_items_from_category('desserts')
    for item in menu_list:
        print(item)


def print_drinks():
    print(
        '''
Drinks
-------'''
    )
    menu_list = get_menu_items_from_category('drinks')
    for item in menu_list:
        print(item)


def user_prompt():
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
        if user_input.lower() in menu.keys():
            menu[user_input.lower()]['orders'] += 1
            print('\n** {1} order of {0} have been added to your meal **'.format(user_input, menu[user_input.lower()]['orders']))
        else:
            print('\nSorry we don\'t carry', user_input)


if __name__ == '__main__':
    main()

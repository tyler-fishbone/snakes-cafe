import uuid

menu = {
    'wings': {
        'category': 'appetizers',
        'orders': 0,
        'price': 10.00,
    },
    'cookies': {
        'category': 'appetizers',
        'orders': 0,
        'price': 10.00,
    },
    'spring rolls': {
        'category': 'appetizers',
        'orders': 0,
        'price': 10.00,
    },
    'brussel sprouts': {
        'category': 'appetizers',
        'orders': 0,
        'price': 10.00,
    },
    'brains': {
        'category': 'appetizers',
        'orders': 0,
        'price': 10.00,
    },
    '6 compliments': {
        'category': 'appetizers',
        'orders': 0,
        'price': 10.00,
    },
    'salmon': {
        'category': 'entrees',
        'orders': 0,
        'price': 10.00,
    },
    'steak': {
        'category': 'entrees',
        'orders': 0,
        'price': 10.00,
    },
    'meat tornado': {
        'category': 'entrees',
        'orders': 0,
        'price': 10.00,
    },
    'a literal garden': {
        'category': 'entrees',
        'orders': 0,
        'price': 10.00,
    },
    'cheeseburger': {
        'category': 'entrees',
        'orders': 0,
        'price': 10.00,
    },
    'lasagne': {
        'category': 'entrees',
        'orders': 0,
        'price': 10.00,
    },
    'cottage cheese': {
        'category': 'sides',
        'orders': 0,
        'price': 10.00,
    },
    'apple sauce': {
        'category': 'sides',
        'orders': 0,
        'price': 10.00,
    },
    'over-ripe banana': {
        'category': 'sides',
        'orders': 0,
        'price': 10.00,
    },
    'freedom fries': {
        'category': 'sides',
        'orders': 0,
        'price': 10.00,
    },
    'pickle': {
        'category': 'sides',
        'orders': 0,
        'price': 10.00,
    },
    'cabbage': {
        'category': 'sides',
        'orders': 0,
        'price': 10.00,
    },
    'ice cream': {
        'category': 'desserts',
        'orders': 0,
        'price': 10.00,
    },
    'cake': {
        'category': 'desserts',
        'orders': 0,
        'price': 10.00,
    },
    'pie': {
        'category': 'desserts',
        'orders': 0,
        'price': 10.00,
    },
    'chocolate spaghetti': {
        'category': 'desserts',
        'orders': 0,
        'price': 10.00,
    },
    'foot massage': {
        'category': 'desserts',
        'orders': 0,
        'price': 10.00,
    },
    'coconut ice cream': {
        'category': 'desserts',
        'orders': 0,
        'price': 10.00,
    },
    'coffee': {
        'category': 'drinks',
        'orders': 0,
        'price': 10.00,
    },
    'tea': {
        'category': 'drinks',
        'orders': 0,
        'price': 10.00,
    },
    'blood of the innocent': {
        'category': 'drinks',
        'orders': 0,
        'price': 10.00,
    },
    'carp saliva': {
        'category': 'drinks',
        'orders': 0,
        'price': 10.00,
    },
    'bacardi 151': {
        'category': 'drinks',
        'orders': 0,
        'price': 10.00,
    },
    'code fellows tap water': {
        'category': 'drinks',
        'orders': 0,
        'price': 10.00,
    },
}

user_uuid = uuid.uuid4()


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
**  To see your order, type "order" **
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
    current_order_subtotal = 0
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
        elif user_input == 'order':
            print(create_reciept(current_order_subtotal))
        elif user_input.lower() in menu.keys():     
            menu[user_input.lower()]['orders'] += 1
            current_order_subtotal = get_total_price_before_tax(current_order_subtotal, user_input.lower())
            print('\n** {1} order of {0} have been added to your meal and your total is ${2} **'.format(user_input, menu[user_input.lower()]['orders'], current_order_subtotal))
        else:
            print('\nSorry we don\'t carry', user_input)


def get_total_price_before_tax(subtotal, ordered_item):
    if ordered_item is '':
        raise SyntaxError('Argument invalid. Must be not be an empty string.')
    if ordered_item not in menu.keys():
        raise LookupError('Argument invalid. Must be valid menu item from menu dict.')
    subtotal += menu[ordered_item]['price']
    return subtotal


def create_list_of_items_ordered():
    list_of_ordered_items = []
    for key, value in menu.items():
        if value['orders'] > 0:
            list_of_ordered_items.append(key)
    if list_of_ordered_items == []:
        raise LookupError('Argument invalid. Must be not be an empty list.')
    return list_of_ordered_items


def get_sales_tax(subtotal):
    return subtotal * .101


def create_reciept(subtotal):
    reciept_string = """
*******************************************
The Snakes Cafe
"Eatability Counts"

Order #{}
===========================================
""".format(user_uuid)

# Wings x1                              $2.00
# Spring Rolls x3                       $7.50
# Steak x1                             $12.00
# Blood of the Innocent x1            $666.66



    reciept_string += '\n-------------------------------------------\n'
    reciept_string += '{:<22s}{:>21s}\n'.format('Subtotal', '${:.2f}'.format(subtotal))
    reciept_string += '{:<22s}{:>21s}\n'.format('Sales Tax', '${:.2f}'.format(get_sales_tax(subtotal)))
    reciept_string += '---------\n'
    reciept_string += '{:<22s}{:>21s}\n'.format('Total Due', '${:.2f}'.format(subtotal + get_sales_tax(subtotal)))
    reciept_string += '*******************************************\n'
    return reciept_string

if __name__ == '__main__':
    main()


# str += '{:<22s}\t\t{}\n'.format(item.title(), '${:.2f}'.format(data[0]))
# {:<26s}{:>12s}
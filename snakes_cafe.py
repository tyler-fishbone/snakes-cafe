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
        'price': 2.00,
    },
    'spring rolls': {
        'category': 'appetizers',
        'orders': 0,
        'price': 7.00,
    },
    'brussel sprouts': {
        'category': 'appetizers',
        'orders': 0,
        'price': 6.00,
    },
    'brains': {
        'category': 'appetizers',
        'orders': 0,
        'price': 100.00,
    },
    '6 compliments': {
        'category': 'appetizers',
        'orders': 0,
        'price': 1.00,
    },
    'salmon': {
        'category': 'entrees',
        'orders': 0,
        'price': 20.00,
    },
    'steak': {
        'category': 'entrees',
        'orders': 0,
        'price': 30.00,
    },
    'meat tornado': {
        'category': 'entrees',
        'orders': 0,
        'price': 15.00,
    },
    'a literal garden': {
        'category': 'entrees',
        'orders': 0,
        'price': 12.00,
    },
    'cheeseburger': {
        'category': 'entrees',
        'orders': 0,
        'price': 10.00,
    },
    'lasagne': {
        'category': 'entrees',
        'orders': 0,
        'price': 14.00,
    },
    'cottage cheese': {
        'category': 'sides',
        'orders': 0,
        'price': 3.00,
    },
    'apple sauce': {
        'category': 'sides',
        'orders': 0,
        'price': 4.00,
    },
    'over-ripe banana': {
        'category': 'sides',
        'orders': 0,
        'price': 2.00,
    },
    'freedom fries': {
        'category': 'sides',
        'orders': 0,
        'price': 6.00,
    },
    'pickle': {
        'category': 'sides',
        'orders': 0,
        'price': 3.00,
    },
    'cabbage': {
        'category': 'sides',
        'orders': 0,
        'price': 5.00,
    },
    'ice cream': {
        'category': 'desserts',
        'orders': 0,
        'price': 7.00,
    },
    'cake': {
        'category': 'desserts',
        'orders': 0,
        'price': 3.00,
    },
    'pie': {
        'category': 'desserts',
        'orders': 0,
        'price': 5.00,
    },
    'chocolate spaghetti': {
        'category': 'desserts',
        'orders': 0,
        'price': 15.00,
    },
    'foot massage': {
        'category': 'desserts',
        'orders': 0,
        'price': 30.00,
    },
    'coconut ice cream': {
        'category': 'desserts',
        'orders': 0,
        'price': 5.00,
    },
    'coffee': {
        'category': 'drinks',
        'orders': 0,
        'price': 3.00,
    },
    'tea': {
        'category': 'drinks',
        'orders': 0,
        'price': 3.00,
    },
    'blood of the innocent': {
        'category': 'drinks',
        'orders': 0,
        'price': 50.00,
    },
    'carp saliva': {
        'category': 'drinks',
        'orders': 0,
        'price': 25.00,
    },
    'bacardi 151': {
        'category': 'drinks',
        'orders': 0,
        'price': 9.00,
    },
    'code fellows tap water': {
        'category': 'drinks',
        'orders': 0,
        'price': 1.00,
    },
}

user_uuid = uuid.uuid4()
list_of_menu_categories = ['appetizers', 'entrees', 'sides', 'desserts', 'drinks']


def main():
    """
    This function is here to kick off the application
    """
    print_whole_menu()
    user_prompt()


def print_header():
    """
    This function prints the header of the menu to the user
    """
    print(
        '''
**********************************************
**        Welcome to the Snakes Cafe!       **
**        Please see our menu below.        **
**                                          **
**      To see your order, type "order"     **
**     To quit at any time, type "quit"     **
**********************************************
        '''
    )


def get_menu_items_from_category(category):
    """
    This function takes a category and returns a list of menu items in it
    """
    menu_item_list = []
    if type(category) is not str:
        raise TypeError('Argument invalid. Must be string.')
    if category not in [data['category'] for data in menu.values()]:
        raise LookupError('Argument invalid. Must be valid category from menu dict.')
    for key, value in menu.items():
        if value['category'] == category:
            menu_item_list.append(key)
    return menu_item_list


def print_whole_menu():
    """
    This function prints all of the menu items for each category
    """
    print_header()
    for item in list_of_menu_categories:
        print_category(item)


def print_category(cat):
    """
    This function takes in a category and prints the items for that category
    """
    if cat not in [data['category'] for data in menu.values()]:
        raise LookupError('Argument invalid. Must be valid category from menu dict.')
    testing_key_list = []
    print(
        '''
{}
-------'''.format(cat.title())
    )
    menu_list = get_menu_items_from_category(cat)
    for item in menu_list:
        testing_key_list.append(item)
        print(item.title())
    return testing_key_list


def remove_single_order(full_remove_string):
    """
    This function removes an order from a menu item when prompted
    """
    for key in menu.keys():
        if key in full_remove_string:
            if menu[key]['orders'] > 0:
                menu[key]['orders'] -= 1
                return key
            else:
                raise ValueError('Cannot remove orders past 0.')


def user_prompt():
    """
    This function handles the user prompt and allows for the input of menu items, categories, menu, and order.
    """
    while True:
        print(
            '''
*******************************************
**     What would you like to order?     **
*******************************************
            '''
        )
        user_input = input('>   ').lower()
        if user_input == 'quit':
            break
        elif user_input == 'order':
            print(create_reciept(get_current_subtotal()))
        elif user_input == 'menu':
            print_whole_menu()
        elif user_input in list_of_menu_categories:
            print_category(user_input)
        elif 'remove ' in user_input:
            key_of_order_removed = remove_single_order(user_input)
            print('\n** 1 order of {0} has been removed from your meal and your total is ${1:.2f} **'.format(key_of_order_removed.title(), get_current_subtotal()))
        elif user_input.lower() in menu.keys():
            menu[user_input.lower()]['orders'] += 1
            # current_order_subtotal = get_total_price_before_tax(current_order_subtotal, user_input.lower())
            print('\n** {1} order of {0} have been added to your meal and your total is ${2:.2f} **'.format(user_input.title(), menu[user_input.lower()]['orders'], get_current_subtotal()))
        else:
            print('\nSorry we don\'t carry', user_input)


def get_current_subtotal():
    """
    This function retrieves the current order's subtotal
    """
    subtotal = 0
    for key in menu:
        subtotal += menu[key]['orders'] * menu[key]['price']
    return subtotal


# def get_total_price_before_tax(subtotal, ordered_item):
#     if ordered_item is '':
#         raise SyntaxError('Argument invalid. Must be not be an empty string.')
#     if ordered_item not in menu.keys():
#         raise LookupError('Argument invalid. Must be valid menu item from menu dict.')
#     subtotal += menu[ordered_item]['price']
#     return subtotal


def create_list_of_items_ordered():
    """
    This function creates a list of the keys of items that have been ordered
    """
    list_of_ordered_items = []
    for key, value in menu.items():
        if value['orders'] > 0:
            list_of_ordered_items.append(key)
    # if list_of_ordered_items == []:
    #     raise LookupError('Argument invalid. Must be not be an empty list.')
    return list_of_ordered_items


def get_sales_tax(subtotal):
    """
    This function calculates the sales tax
    """
    if type(subtotal) is str:
        raise TypeError('Argument invalid. Must be number.')
    return subtotal * .101


def create_reciept(subtotal):
    """
    This function assembles and prints the reciept for the user
    """
    reciept_string = """
*******************************************
The Snakes Cafe
"Eatability Counts"

Order #{}
===========================================

""".format(user_uuid)

    items_ordered = create_list_of_items_ordered()
    for key in items_ordered:
        order_amount_string = key.title() + ' x' + str(menu[key]['orders'])
        reciept_string += '{:<32s}{:>11s}\n'.format(order_amount_string, '${:.2f}'.format(menu[key]['price']))

    reciept_string += '\n-------------------------------------------\n'
    reciept_string += '{:<22s}{:>21s}\n'.format('Subtotal', '${:.2f}'.format(subtotal))
    reciept_string += '{:<22s}{:>21s}\n'.format('Sales Tax', '${:.2f}'.format(get_sales_tax(subtotal)))
    reciept_string += '---------\n'
    reciept_string += '{:<22s}{:>21s}\n'.format('Total Due', '${:.2f}'.format(subtotal + get_sales_tax(subtotal)))
    reciept_string += '*******************************************\n'
    return reciept_string

if __name__ == '__main__':
    main()

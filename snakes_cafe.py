import uuid
import csv


class Order:


    def __init__(self):
        self.menu = {
            'fries': {
                'category': 'appetizers',
                'orders': 0,
                'price': 10.00,
                'stock': 10,
            },
            'cooties': {
                'category': 'appetizers',
                'orders': 0,
                'price': 2.00,
                'stock': 10,
            },
            'fruit roll ups': {
                'category': 'appetizers',
                'orders': 0,
                'price': 7.00,
                'stock': 10,
            },
            'wings': {
                'category': 'appetizers',
                'orders': 0,
                'price': 10.00,
                'stock': 10,
            },
            'cookies': {
                'category': 'appetizers',
                'orders': 0,
                'price': 2.00,
                'stock': 10,
            },
            'spring rolls': {
                'category': 'appetizers',
                'orders': 0,
                'price': 7.00,
                'stock': 10,
            },
            'brussel sprouts': {
                'category': 'appetizers',
                'orders': 0,
                'price': 6.00,
                'stock': 10,
            },
            'brains': {
                'category': 'appetizers',
                'orders': 0,
                'price': 100.00,
                'stock': 10,
            },
            '6 compliments': {
                'category': 'appetizers',
                'orders': 0,
                'price': 1.00,
                'stock': 10,
            },
            'broccoli soup': {
                'category': 'appetizers',
                'orders': 0,
                'price': 5.00,
                'stock': 10,
            },
            'bird eyes': {
                'category': 'appetizers',
                'orders': 0,
                'price': 37.00,
                'stock': 10,
            },
            'fingernail nachos': {
                'category': 'appetizers',
                'orders': 0,
                'price': 15.00,
                'stock': 10,
            },
            'whale': {
                'category': 'entrees',
                'orders': 0,
                'price': 100.00,
                'stock': 10,
            },
            'owl': {
                'category': 'entrees',
                'orders': 0,
                'price': 70.00,
                'stock': 10,
            },
            'shark fin soup': {
                'category': 'entrees',
                'orders': 0,
                'price': 55.00,
                'stock': 10,
            },
            'ostrich': {
                'category': 'entrees',
                'orders': 0,
                'price': 20.00,
                'stock': 10,
            },
            'dolphin': {
                'category': 'entrees',
                'orders': 0,
                'price': 70.00,
                'stock': 10,
            },
            'turtle soup': {
                'category': 'entrees',
                'orders': 0,
                'price': 55.00,
                'stock': 10,
            },
            'salmon': {
                'category': 'entrees',
                'orders': 0,
                'price': 20.00,
                'stock': 10,
            },
            'steak': {
                'category': 'entrees',
                'orders': 0,
                'price': 30.00,
                'stock': 10,
            },
            'meat tornado': {
                'category': 'entrees',
                'orders': 0,
                'price': 15.00,
                'stock': 10,
            },
            'a literal garden': {
                'category': 'entrees',
                'orders': 0,
                'price': 12.00,
                'stock': 10,
            },
            'cheeseburger': {
                'category': 'entrees',
                'orders': 0,
                'price': 10.00,
                'stock': 10,
            },
            'lasagne': {
                'category': 'entrees',
                'orders': 0,
                'price': 14.00,
                'stock': 10,
            },
            'cauliflower soup': {
                'category': 'sides',
                'orders': 0,
                'price': 7.00,
                'stock': 10,
            },
            'dead skin': {
                'category': 'sides',
                'orders': 0,
                'price': 9.00,
                'stock': 10,
            },
            "austin's cough": {
                'category': 'sides',
                'orders': 0,
                'price': 7.00,
                'stock': 10,
            },
            'pineapple wedges': {
                'category': 'sides',
                'orders': 0,
                'price': 7.00,
                'stock': 10,
            },
            'seaweed salad': {
                'category': 'sides',
                'orders': 0,
                'price': 9.00,
                'stock': 10,
            },
            'spring mix': {
                'category': 'sides',
                'orders': 0,
                'price': 7.00,
                'stock': 10,
            },
            'cottage cheese': {
                'category': 'sides',
                'orders': 0,
                'price': 3.00,
                'stock': 10,
            },
            'apple sauce': {
                'category': 'sides',
                'orders': 0,
                'price': 4.00,
                'stock': 10,
            },
            'overripe banana': {
                'category': 'sides',
                'orders': 0,
                'price': 2.00,
                'stock': 10,
            },
            'freedom fries': {
                'category': 'sides',
                'orders': 0,
                'price': 6.00,
                'stock': 10,
            },
            'pickle': {
                'category': 'sides',
                'orders': 0,
                'price': 3.00,
                'stock': 10,
            },
            'cabbage': {
                'category': 'sides',
                'orders': 0,
                'price': 5.00,
                'stock': 10,
            },
            'subway cookie': {
                'category': 'desserts',
                'orders': 0,
                'price': 15.00,
                'stock': 10,
            },
            'spoonful of sugar': {
                'category': 'desserts',
                'orders': 0,
                'price': 9.00,
                'stock': 10,
            },
            'a book damnit': {
                'category': 'desserts',
                'orders': 0,
                'price': 8.00,
                'stock': 10,
            },
            'birthday cake and song': {
                'category': 'desserts',
                'orders': 0,
                'price': 15.00,
                'stock': 10,
            },
            'cherry pie': {
                'category': 'desserts',
                'orders': 0,
                'price': 9.00,
                'stock': 10,
            },
            'cheesecake': {
                'category': 'desserts',
                'orders': 0,
                'price': 8.00,
                'stock': 10,
            },
            'ice cream': {
                'category': 'desserts',
                'orders': 0,
                'price': 7.00,
                'stock': 10,
            },
            'cake': {
                'category': 'desserts',
                'orders': 0,
                'price': 3.00,
                'stock': 10,
            },
            'pie': {
                'category': 'desserts',
                'orders': 0,
                'price': 5.00,
                'stock': 10,
            },
            'chocolate spaghetti': {
                'category': 'desserts',
                'orders': 0,
                'price': 15.00,
                'stock': 10,
            },
            'foot massage': {
                'category': 'desserts',
                'orders': 0,
                'price': 30.00,
                'stock': 10,
            },
            'coconut ice cream': {
                'category': 'desserts',
                'orders': 0,
                'price': 5.00,
                'stock': 10,
            },
            'sewer water': {
                'category': 'drinks',
                'orders': 0,
                'price': 3.00,
                'stock': 10,
            },
            'dehydrated water': {
                'category': 'drinks',
                'orders': 0,
                'price': 8.00,
                'stock': 10,
            },
            'river ganges water': {
                'category': 'drinks',
                'orders': 0,
                'price': 9.00,
                'stock': 10,
            },
            'bud light': {
                'category': 'drinks',
                'orders': 0,
                'price': 3.00,
                'stock': 10,
            },
            'gargled lemonade': {
                'category': 'drinks',
                'orders': 0,
                'price': 8.00,
                'stock': 10,
            },
            'mango lassi': {
                'category': 'drinks',
                'orders': 0,
                'price': 9.00,
                'stock': 10,
            },
            'coffee': {
                'category': 'drinks',
                'orders': 0,
                'price': 3.00,
                'stock': 10,
            },
            'tea': {
                'category': 'drinks',
                'orders': 0,
                'price': 3.00,
                'stock': 10,
            },
            'blood of the innocent': {
                'category': 'drinks',
                'orders': 0,
                'price': 50.00,
                'stock': 10,
            },
            'carp saliva': {
                'category': 'drinks',
                'orders': 0,
                'price': 25.00,
                'stock': 10,
            },
            'bacardi': {
                'category': 'drinks',
                'orders': 0,
                'price': 9.00,
                'stock': 10,
            },
            'code fellows tap water': {
                'category': 'drinks',
                'orders': 0,
                'price': 1.00,
                'stock': 10,
            },
        }

        self.user_uuid = uuid.uuid4()
        self.set_of_menu_categories = set()


    def main(self):
        """
        This function is here to kick off the application
        """
        self.new_menu_or_default()
        self.print_whole_menu()
        self.user_prompt()


    def new_menu_or_default(self):
        """
        gives the user an option to put in their own menu
        """
        # global set_of_menu_categories
        print('Would you like to use our default menu or enter your own? \
        \n If you would like to use your own please enter a valid file path to the csv. \
        \n If not, just press "enter"')
        user_menu_input = input('>  ')
        if user_menu_input == '':
            print('Continuing with default menu')
        else:
            self.get_alt_menu(user_menu_input)
        self.set_of_menu_categories = {data['category'] for data in self.menu.values()}


    def get_alt_menu(self, file_path_input):
        """
        function that reads input csv file at inputted path and creates a dict from it
        then replaces the default menu with that valye
        """
        # global menu
        alt_menu = {}
        # './alt_menu.csv'  
        try:
            with open(file_path_input, 'r') as f:
                output = csv.reader(f)
                for row in output:
                    print(row)
                    alt_menu[row[0]] = {
                                'category': row[1],
                                'orders': 0,
                                'price': float(row[2]),
                                'stock': int(row[3]),
                            }
                self.menu = alt_menu
                return self.menu
        except FileNotFoundError:
            print('\nNot a valid filepath, going ahead with default menu')
        except IndexError:
            print('\nNot a valid file format, going ahead with default menu')

            


    def print_header(self):
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
**      To remove an item or multiple,      **
**  type "remove (item) / remove #-(items)" **
**         To order multiple items,         **
**           type "#-(item name)"           **
**********************************************
        '''
        )


    def get_menu_items_from_category(self, category):
        """
        This function takes a category and returns a list of menu items in it
        """
        menu_item_list = []
        if type(category) is not str:
            raise TypeError('Argument invalid. Must be string.')
        if category not in [data['category'] for data in self.menu.values()]:
            raise LookupError('Argument invalid. Must be valid category from menu dict.')
        for key, value in self.menu.items():
            if value['category'] == category:
                menu_item_list.append(key)
        return menu_item_list


    def print_whole_menu(self):
        """
        This function prints all of the menu items for each category
        """
        self.print_header()
        for item in self.set_of_menu_categories:
            self.print_category(item)


    def print_category(self, cat):
        """
        This function takes in a category and prints the items for that category
        """
        if cat not in [data['category'] for data in self.menu.values()]:
            raise LookupError('Argument invalid. Must be valid category from menu dict.')
        testing_key_list = []
        print(
            '''
{}
-------'''.format(cat.title())
        )
        menu_list = self.get_menu_items_from_category(cat)
        for item in menu_list:
            testing_key_list.append(item)
            print(item.title())
        return testing_key_list


    def remove_item(self, full_remove_string):
        """
        This function removes an order from a menu item when prompted
        """
        for key in self.menu.keys():
            if '-' in full_remove_string and key in full_remove_string:
                user_input_list = full_remove_string.split('-')
                split_2_list = user_input_list[0].split(' ')
                if (self.menu[user_input_list[1].lower()]['orders'] - int(split_2_list[1])) >= 0:
                    self.menu[user_input_list[1].lower()]['orders'] -= int(split_2_list[1])
                    self.menu[user_input_list[1].lower()]['stock'] += int(split_2_list[1])
                    print('\n** {0} orders of {1} have been removed from your meal and your total is ${2} **'.format(split_2_list[1], user_input_list[1].title(), self.get_current_subtotal()))
                else:
                    print('\nCannot remove orders past 0')
                return user_input_list
            elif key in full_remove_string:
                if self.menu[key]['orders'] > 0:
                    self.menu[key]['orders'] -= 1
                    self.menu[key]['stock'] += 1
                    key_of_order_removed = key
                    print('\n** 1 order of {0} has been removed from your meal and your total is ${1:.2f} **'.format(key_of_order_removed.title(), self.get_current_subtotal()))
                    return key
                else:
                    print('\nCannot remove orders past 0')
                    return key
        print("\nTo remove an item enter 'remove #-(item name)'")


    def add_item(self, user_input_prm):
        if self.menu[user_input_prm]['stock'] > 0:
            self.menu[user_input_prm.lower()]['orders'] += 1
            self.menu[user_input_prm.lower()]['stock'] -= 1
            print('\n** 1 order of {0} has been added to your meal and your total is ${2:.2f} **'.format(user_input_prm.title(), self.menu[user_input_prm.lower()]['orders'], self.get_current_subtotal()))
        else:
            print('\nSorry quantity exceeds our stock for that item')


    def add_multiple_orders(self, user_input_prm):
        """
        This function allows the user to add multiple orders
        """
        try: 
            user_input_list = user_input_prm.split('-')
            if (self.menu[user_input_list[1].lower()]['stock'] - int(user_input_list[0])) >= 0:
                self.menu[user_input_list[1].lower()]['orders'] += int(user_input_list[0])
                self.menu[user_input_list[1].lower()]['stock'] -= int(user_input_list[0])
                print('\n** {1} orders of {0} have been added to your meal and your total is ${2} **'.format(user_input_list[1].title(), user_input_list[0], self.get_current_subtotal()))
                return user_input_list
            else:
                print('\nSorry quantity exceeds our stock for that item')
        except ValueError:
            print('\nSorry, we do not know what you mean, use format #-items')
        except KeyError:
            print('\nSorry, we do not know what you mean, use format #-items')


    def user_prompt(self):
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
            # allow user to give new menu for use in program - extend menu? Need clarification
            elif user_input == 'order':
                print(self.display_order(self.get_current_subtotal()))
            elif user_input == 'menu':
                self.print_whole_menu()
            elif user_input in self.set_of_menu_categories:
                self.print_category(user_input)
            elif 'remove ' in user_input:
                self.remove_item(user_input)
            elif user_input.lower() in self.menu.keys():
                self.add_item(user_input)
            elif '-' in user_input:
                self.add_multiple_orders(user_input)
            else:
                print('\nSorry we don\'t carry', user_input)


    def get_current_subtotal(self):
        """
        This function retrieves the current order's subtotal
        """
        subtotal = 0
        for key in self.menu:
            subtotal += self.menu[key]['orders'] * self.menu[key]['price']
        return subtotal


    def create_list_of_items_ordered(self):
        """
        This function creates a list of the keys of items that have been ordered
        """
        list_of_ordered_items = []
        for key, value in self.menu.items():
            if value['orders'] > 0:
                list_of_ordered_items.append(key)
        # if list_of_ordered_items == []:
        #     raise LookupError('Argument invalid. Must be not be an empty list.')
        return list_of_ordered_items


    def get_sales_tax(self, subtotal):
        """
        This function calculates the sales tax
        """
        if type(subtotal) is str:
            raise TypeError('Argument invalid. Must be number.')
        return subtotal * .101


    def display_order(self, subtotal):
        """
        This function assembles and prints the reciept for the user
        """
        reciept_string = """
*******************************************
The Snakes Cafe
"Eatability Counts"

Order #{}
===========================================

""".format(self.user_uuid)

        items_ordered = self.create_list_of_items_ordered()
        for key in items_ordered:
            order_amount_string = key.title() + ' x' + str(self.menu[key]['orders'])
            reciept_string += '{:<32s}{:>11s}\n'.format(order_amount_string, '${:.2f}'.format(self.menu[key]['price']))

        reciept_string += '\n-------------------------------------------\n'
        reciept_string += '{:<22s}{:>21s}\n'.format('Subtotal', '${:.2f}'.format(subtotal))
        reciept_string += '{:<22s}{:>21s}\n'.format('Sales Tax', '${:.2f}'.format(self.get_sales_tax(subtotal)))
        reciept_string += '---------\n'
        reciept_string += '{:<22s}{:>21s}\n'.format('Total Due', '${:.2f}'.format(subtotal + self.get_sales_tax(subtotal)))
        reciept_string += '*******************************************\n'
        return reciept_string

if __name__ == '__main__':
    try:
        order = Order()
        order.main()
    except (KeyboardInterrupt, EOFError):
        print(" <-- It's 'quit' asshole. Read the directions.")



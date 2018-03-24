import snakes_cafe
import pytest

# get_menu_items_from_category


def test_get_menu_items_from_valid_category(order_class):
    """
    test that items from the correct category are return when that category is input into the function
    """
    assert order_class.get_menu_items_from_category('drinks') == ['sewer water', 'dehydrated water', 'river ganges water', 'bud light', 'gargled lemonade', 'mango lassi', 'coffee', 'tea', 'blood of the innocent', 'carp saliva', 'bacardi', 'code fellows tap water',]


def test_get_menu_items_from_invalid_category(order_class):
    """
    if user or program inputs an invalid into this function it handles the lookup error
    """
    with pytest.raises(LookupError) as err:
        order_class.get_menu_items_from_category('car')

    assert str(err.value) == 'Argument invalid. Must be valid category from menu dict.'


def test_get_menu_items_from_int(order_class):
    """
    handle exception raised if user were to enter in an integer to the function that gets menu items
    from a specific category
    """
    with pytest.raises(TypeError) as err:
        order_class.get_menu_items_from_category(1)

    assert str(err.value) == 'Argument invalid. Must be string.'

# check total order cost is correct


# def test_get_total_price_before_tax_with_valid_entry(order_class):
#     current_order_subtotal = 20
#     assert order_class.get_total_price_before_tax(current_order_subtotal, 'wings') == 30


# def test_get_total_price_before_tax_with_invalid_string(order_class):
#     current_order_subtotal = 20
#     with pytest.raises(LookupError) as err:
#         order_class.get_total_price_before_tax(current_order_subtotal, 'car')

#     assert str(err.value) == 'Argument invalid. Must be valid menu item from menu dict.'


# def test_get_total_price_before_tax_with_no_input(order_class):
#     current_order_subtotal = 20
#     with pytest.raises(SyntaxError) as err:
#         order_class.get_total_price_before_tax(current_order_subtotal, '')

#     assert str(err.value) == 'Argument invalid. Must be not be an empty string.'


# create_list_of_items_ordered


def test_make_list_of_keys_of_orders_greater_than_zero(order_class):
    """
    tests function that generates a list of all the items with an order number greater than zero.
    this function does this by adding an order of wings to the menu dict (which starts at zero),
    runs the function, then resets the orders key back to 0 for wings
    """
    order_class.menu['wings']['orders'] += 1
    assert order_class.create_list_of_items_ordered() == ['wings']
    order_class.menu['wings']['orders'] = 0


def test_no_orders_greater_than_zero_then_cannot_make_list(order_class):
    assert order_class.create_list_of_items_ordered() == []

# print_category


def test_print_category_valid_category(order_class):
    """
    test that items from the correct category are return when that category is input into the function
    """
    assert order_class.print_category('drinks') == ['sewer water', 'dehydrated water', 'river ganges water', 'bud light', 'gargled lemonade', 'mango lassi', 'coffee', 'tea', 'blood of the innocent', 'carp saliva', 'bacardi', 'code fellows tap water',]


def test_print_category_invalid_category(order_class):
    """
    if user or program inputs an invalid into this function it handles the lookup error
    """
    with pytest.raises(LookupError) as err:
        order_class.print_category('car')

    assert str(err.value) == 'Argument invalid. Must be valid category from menu dict.'


# remove_single_order


def test_valid_removal(order_class):
    """
    asserts that when remove single order function is run that the key of the removed item is returned
    """
    order_class.menu['wings']['orders'] = 1
    assert order_class.remove_item('remove wings') == 'wings'


def test_cannot_remove_orders_less_than_zero(order_class):
    """
    handles exception if customer tries to remove an item order when it is already at 0
    """
    assert order_class.remove_item('remove wings') == 'wings'


# get_current_subtotal


def test_zero_subtotal(order_class):
    """
    asserts get_current_subtotal returns zero before any orders are placed
    """
    assert order_class.get_current_subtotal() == 0.0


def test_positive_subtotal(order_class):
    """
    test subtotal when customer has made an order. resets total afterwards.
    """
    order_class.menu['wings']['orders'] = 1
    assert order_class.get_current_subtotal() == 10.00
    order_class.menu['wings']['orders'] = 0


# get_sales_tax


def test_sales_tax(order_class):
    """
    asserts subtotal is being calculated correctly
    """
    assert order_class.get_sales_tax(20.00) == 2.02


def test_invalid_sales_tax(order_class):
    """
    handles exceptions where an incorrect type is passed into the get_sales_tax function
    """
    with pytest.raises(TypeError) as err:
        order_class.get_sales_tax('car')

    assert str(err.value) == 'Argument invalid. Must be number.'


# add_multiple_orders


def test_add_multiple_orders_valid_int(order_class):
    """
    asserts that correct values are parsed from user input
    """
    assert order_class.add_multiple_orders('5-wings') == ['5', 'wings']


def test_add_multiple_orders_invalid_float(order_class):
    """
    asserts floats cannot be used as values to add
    """
    assert order_class.add_multiple_orders('5.5-wings') is None


# get_alt_menu


def test_get_alt_menu_with_valid_filepath(order_class):
    """
    asserts that menu returned is from input csv file
    """
    assert order_class.get_alt_menu('./alt_menu.csv') == {'wings': {'category': 'appetizers', 'orders': 0, 'price': 10.0, 'stock': 10}, 'koolaid': {'category': 'drinks', 'orders': 0, 'price': 2.0, 'stock': 10}, 'popcorn': {'category': 'appetizers', 'orders': 0, 'price': 3.0, 'stock': 10}, 'chicken': {'category': 'entrees', 'orders': 0, 'price': 15.0, 'stock': 10}, 'chili con carne': {'category': 'entrees', 'orders': 0, 'price': 9.0, 'stock': 10}, 'dried pineapple': {'category': 'desserts', 'orders': 0, 'price': 4.0, 'stock': 10}, 'tree bark': {'category': 'sides', 'orders': 0, 'price': 6.0, 'stock': 10}}


def test_get_alt_menu_with_invalid_filepath(order_class):
    """
    asserts that menu returned is from a nonexistent file path returns none
    """
    assert order_class.get_alt_menu('hsdfl') is None


def test_get_alt_menu_with_invalid_csv_format(order_class):
    """
    asserts that menu returned is from a non csv file returns none
    """
    assert order_class.get_alt_menu('./test_plan.md') is None


# class test

def test_make_new_order_obj_test_menu_exist(order_class):
    assert order_class.menu['wings']['orders'] == 0


#len


def test_len_returns_valid_len(order_class):
    assert len(order_class) == 0


def test_len_when_greater_than_zero(order_class):
    order_class.menu['wings']['orders'] = 2
    assert len(order_class) == 2

# repr

def test_repr_against_expected_output(order_class):
    assert order_class.__repr__() == '<Order #{} | Items: {} | Total: {}>'.format(order_class.user_uuid, 0, 0.0)

def test_repr_against_expected_output_with_inventory(order_class):
    order_class.menu['wings']['orders'] = 2
    assert order_class.__repr__() == '<Order #{} | Items: {} | Total: {}>'.format(order_class.user_uuid, 2, 22.02)


#str

def test_str_method_on_class_valid(order_class):
    assert str(order_class) == '''
*******************************************
The Snakes Cafe
"Eatability Counts"

Order #{}
===========================================


-------------------------------------------
Subtotal                              $0.00
Sales Tax                             $0.00
---------
Total Due                             $0.00
*******************************************
'''.format(order_class.user_uuid)


def test_str_method_on_class_valid_with_inventory(order_class):
    order_class.menu['wings']['orders'] = 2
    assert str(order_class) == '''
*******************************************
The Snakes Cafe
"Eatability Counts"

Order #{}
===========================================

Wings x2                             $10.00

-------------------------------------------
Subtotal                             $20.00
Sales Tax                             $2.02
---------
Total Due                            $22.02
*******************************************
'''.format(order_class.user_uuid)


# add item

def test_add_item_valid_input(order_class):
    assert order_class.add_item('wings') == 'wings'


def test_add_item_invalid_input(order_class):
    assert order_class.add_item('car') is None


# total items


def test_total_item_with_none_valid(order_class):
    assert order_class.total_items() == 0


def test_total_item_with_seven_valid(order_class):
    order_class.menu['wings']['orders'] = 2
    order_class.menu['whale']['orders'] = 5
    assert order_class.total_items() == 7

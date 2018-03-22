import snakes_cafe
import pytest

# get_menu_items_from_category


def test_get_menu_items_from_valid_category():
    """
    test that items from the correct category are return when that category is input into the function
    """
    assert snakes_cafe.get_menu_items_from_category('drinks') == ['coffee', 'tea', 'blood of the innocent', 'carp saliva', 'bacardi 151', 'code fellows tap water']


def test_get_menu_items_from_invalid_category():
    """
    if user or program inputs an invalid into this function it handles the lookup error
    """
    with pytest.raises(LookupError) as err:
        snakes_cafe.get_menu_items_from_category('car')

    assert str(err.value) == 'Argument invalid. Must be valid category from menu dict.'


def test_get_menu_items_from_int():
    """
    handle exception raised if user were to enter in an integer to the function that gets menu items
    from a specific category
    """
    with pytest.raises(TypeError) as err:
        snakes_cafe.get_menu_items_from_category(1)

    assert str(err.value) == 'Argument invalid. Must be string.'

# check total order cost is correct


# def test_get_total_price_before_tax_with_valid_entry():
#     current_order_subtotal = 20
#     assert snakes_cafe.get_total_price_before_tax(current_order_subtotal, 'wings') == 30


# def test_get_total_price_before_tax_with_invalid_string():
#     current_order_subtotal = 20
#     with pytest.raises(LookupError) as err:
#         snakes_cafe.get_total_price_before_tax(current_order_subtotal, 'car')

#     assert str(err.value) == 'Argument invalid. Must be valid menu item from menu dict.'


# def test_get_total_price_before_tax_with_no_input():
#     current_order_subtotal = 20
#     with pytest.raises(SyntaxError) as err:
#         snakes_cafe.get_total_price_before_tax(current_order_subtotal, '')

#     assert str(err.value) == 'Argument invalid. Must be not be an empty string.'


# create_list_of_items_ordered


def test_make_list_of_keys_of_orders_greater_than_zero():
    """
    tests function that generates a list of all the items with an order number greater than zero.
    this function does this by adding an order of wings to the menu dict (which starts at zero),
    runs the function, then resets the orders key back to 0 for wings
    """
    snakes_cafe.menu['wings']['orders'] += 1
    assert snakes_cafe.create_list_of_items_ordered() == ['wings']
    snakes_cafe.menu['wings']['orders'] = 0


# def test_no_orders_greater_than_zero_then_cannot_make_list():
#     with pytest.raises(LookupError) as err:
#         snakes_cafe.create_list_of_items_ordered()

#     assert str(err.value) == 'Argument invalid. Must be not be an empty list.'

# print_category


def test_valid_category():
    """
    test that items from the correct category are return when that category is input into the function
    """
    assert snakes_cafe.print_category('appetizers') == ['wings', 'cookies', 'spring rolls', 'brussel sprouts', 'brains', '6 compliments']


def test_invalid_category():
    """
    if user or program inputs an invalid into this function it handles the lookup error
    """
    with pytest.raises(LookupError) as err:
        snakes_cafe.print_category('car')

    assert str(err.value) == 'Argument invalid. Must be valid category from menu dict.'


# remove_single_order


def test_valid_removal():
    """
    asserts that when remove single order function is run that the key of the removed item is returned
    """
    snakes_cafe.menu['wings']['orders'] = 1
    assert snakes_cafe.remove_single_order('remove wings') == 'wings'


def test_cannot_remove_orders_less_than_zero():
    """
    handles exception if customer tries to remove an item order when it is already at 0
    """
    with pytest.raises(ValueError) as err:
        snakes_cafe.remove_single_order('remove wings')

    assert str(err.value) == 'Cannot remove orders past 0.'


# get_current_subtotal


def test_zero_subtotal():
    """
    asserts get_current_subtotal returns zero before any orders are placed
    """
    assert snakes_cafe.get_current_subtotal() == 0.0


def test_positive_subtotal():
    """
    test subtotal when customer has made an order. resets total afterwards.
    """
    snakes_cafe.menu['wings']['orders'] = 1
    assert snakes_cafe.get_current_subtotal() == 10.00
    snakes_cafe.menu['wings']['orders'] = 0


# get_sales_tax


def test_sales_tax():
    """
    asserts subtotal is being calculated correctly
    """
    assert snakes_cafe.get_sales_tax(20.00) == 2.02


def test_invalid_sales_tax():
    """
    handles exceptions where an incorrect type is passed into the get_sales_tax function
    """
    with pytest.raises(TypeError) as err:
        snakes_cafe.get_sales_tax('car')

    assert str(err.value) == 'Argument invalid. Must be number.'

import snakes_cafe
import pytest

# get_menu_items_from_category


def test_get_menu_items_from_valid_category():
    assert snakes_cafe.get_menu_items_from_category('drinks') == ['coffee', 'tea', 'blood of the innocent', 'carp saliva', 'bacardi 151', 'code fellows tap water']


def test_get_menu_items_from_invalid_category():
    with pytest.raises(LookupError) as err:
        snakes_cafe.get_menu_items_from_category('car')

    assert str(err.value) == 'Argument invalid. Must be valid category from menu dict.'


def test_get_menu_items_from_int():
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
    snakes_cafe.menu['wings']['orders'] += 1
    assert snakes_cafe.create_list_of_items_ordered() == ['wings']
    snakes_cafe.menu['wings']['orders'] = 0


# def test_no_orders_greater_than_zero_then_cannot_make_list():
#     with pytest.raises(LookupError) as err:
#         snakes_cafe.create_list_of_items_ordered()

#     assert str(err.value) == 'Argument invalid. Must be not be an empty list.'

# print_category


def test_valid_category():
    assert snakes_cafe.print_category('appetizers') == ['wings', 'cookies', 'spring rolls', 'brussel sprouts', 'brains', '6 compliments']


def test_invalid_category():
    with pytest.raises(LookupError) as err:
        snakes_cafe.print_category('car')

    assert str(err.value) == 'Argument invalid. Must be valid category from menu dict.'


# remove_single_order


def test_valid_removal():
    snakes_cafe.menu['wings']['orders'] = 1
    assert snakes_cafe.remove_single_order('remove wings') == 'wings'


def test_cannot_remove_orders_less_than_zero():
    with pytest.raises(ValueError) as err:
        snakes_cafe.remove_single_order('remove wings')

    assert str(err.value) == 'Cannot remove orders past 0.'


# get_current_subtotal


def test_zero_subtotal():
    assert snakes_cafe.get_current_subtotal() == 0.0


def test_positive_subtotal():
    snakes_cafe.menu['wings']['orders'] = 1
    assert snakes_cafe.get_current_subtotal() == 10.00
    snakes_cafe.menu['wings']['orders'] = 0


# get_sales_tax


def test_sales_tax():
    assert snakes_cafe.get_sales_tax(20.00) == 2.02


def test_invalid_sales_tax():
    with pytest.raises(TypeError) as err:
        snakes_cafe.get_sales_tax('car')

    assert str(err.value) == 'Argument invalid. Must be number.'

import snakes_cafe
import pytest


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

## check total order cost is correct

def test_get_total_price_before_tax_with_valid_entry():
    current_order_subtotal = 20
    assert snakes_cafe.get_total_price_before_tax(current_order_subtotal, 'wings') == 30


def test_get_total_price_before_tax_with_invalid_string():
    current_order_subtotal = 20
    with pytest.raises(LookupError) as err:
        snakes_cafe.get_total_price_before_tax(current_order_subtotal, 'car')

    assert str(err.value) == 'Argument invalid. Must be valid menu item from menu dict.'


def test_get_total_price_before_tax_with_no_input():
    current_order_subtotal = 20
    with pytest.raises(SyntaxError) as err:
        snakes_cafe.get_total_price_before_tax(current_order_subtotal, '')

    assert str(err.value) == 'Argument invalid. Must be not be an empty string.'

# def test_get_total_price_before_tax_with_negative_price():
#     menu = {
#         'wings': {
#             'category': 'appetizers',
#             'orders': 0,
#             'prices': -10.00,
#         }
#     }
#     current_order_subtotal = 20
#     with pytest.raises(ArithmeticError) as err:
#         snakes_cafe.get_total_price_before_tax(current_order_subtotal, 'wings')

#     assert str(err.value) == 'Argument invalid. Price must be above 0.'


# def test_get_total_price_before_tax_with_no_price():
#     menu = {
#         'wings': {
#             'category': 'appetizers',
#             'orders': 0,
#         }
#     }
#     current_order_subtotal = 20
#     with pytest.raises(LookupError) as err:
#         snakes_cafe.get_total_price_before_tax(current_order_subtotal, 'wings')

#     assert str(err.value) == 'Argument invalid. Price must exist as key.'


## check list of items ordered


def test_make_list_of_keys_of_orders_greater_than_zero():
    snakes_cafe.menu['wings']['orders'] += 1
    assert snakes_cafe.create_list_of_items_ordered() == ['wings']
    snakes_cafe.menu['wings']['orders'] = 0


def test_no_orders_greater_than_zero_then_cannot_make_list():
    with pytest.raises(LookupError) as err:
        snakes_cafe.create_list_of_items_ordered()

    assert str(err.value) == 'Argument invalid. Must be not be an empty list.'
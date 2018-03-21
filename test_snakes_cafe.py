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
    
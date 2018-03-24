import pytest
import snakes_cafe

@pytest.fixture
def order_class():
    return snakes_cafe.Order()

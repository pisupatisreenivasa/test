# test_shopping_cart.py
import pytest
from Shopping_cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_item(cart):
    cart.add_item("Product A", 10)
    assert cart.items == [{"item": "Product A", "price": 10}]

def test_remove_item(cart):
    cart.add_item("Product A", 10)
    cart.add_item("Product B", 20)
    cart.remove_item("Product A")
    assert cart.items == [{"item": "Product B", "price": 20}]

def test_calculate_total_price(cart):
    cart.add_item("Product A", 10)
    cart.add_item("Product B", 20)
    assert cart.calculate_total_price() == 30

def test_apply_discount(cart):
    cart.add_item("Product A", 10)
    cart.add_item("Product B", 20)
    cart.apply_discount(10)
    assert cart.items == [{"item": "Product A", "price": 9}, {"item": "Product B", "price": 18}]

def test_apply_discount_invalid_value(cart):
    with pytest.raises(ValueError):
        cart.apply_discount(-10)

if __name__ == "__main__":
    pytest.main()


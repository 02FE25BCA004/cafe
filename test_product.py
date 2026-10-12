from product import get_product_info
def test_get_product_info():
    result = get_product_info(101, "Laptop", 2, 50000)
    expected = {
        "Product_id: 101\n"
        "Name: Laptop\n"
        "Quantity: 2\n"
        "Price: 50000\n"
    }
    assert result == expected
import json
from products import Product
from cart import dao

class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> 'Cart':
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    product_ids = []
    for cart_detail in cart_details:
        try:
            contents = json.loads(cart_detail['contents'])
            product_ids.extend(contents)
        except json.JSONDecodeError:
            continue  # Handle invalid JSON gracefully

    products_list = [Product.get_product(product_id) for product_id in product_ids]
    return products_list


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
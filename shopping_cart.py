#  The typing module provides support for type hints. Type hints are optional annotations that specify the expected data types of variables, function parameters, and return values.
# List[str] means a list where all elements are strings, and List[int] means a list of integers.
# TLDR; this just allows you to have some type checking in your code compared to using the default python list like x = [1, 2, 3]
from typing import List


# We're using a shopping cart class as example
class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        # pass
        # instantiate an empty list of strings
        self.items: List[str] = [] 
        self.max_size = max_size

    def add(self, item: str) -> None:
        # check if current size of cart is already max (if it is and you run the add method, then we should raise an error)
        if self.size() == self.max_size:
            raise OverflowError("Max size of cart reached. Cannot add more items.")
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        # pass
        return self.items

    def get_total_price(self, price_map: dict) -> float:
        total_price = 0
        for item in price_map:
            total_price += price_map[item]
        return total_price
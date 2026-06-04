def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

#typing_module
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

#any_typing_for_function's
from typing import Any
def some_function(data: Any):
    print(data)


print(get_full_name("john", "doe"))
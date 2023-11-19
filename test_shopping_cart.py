# when you type 'pytest' in terminal, pytest looks at your directory for files with the word 'test' to determine if it should run the file as unit test
# typically, by convention, you'd name test_my_class.py to test a file called my_class.py

from shopping_cart import ShoppingCart
import pytest

'''
What are mocks?
Mocks are objects that simulate the behavior of real objects. They are commonly used for testing purposes.
i.e. in real world application, you may need to instantiate a connection to a database, or have some random function that returns a random value.

This is hard to replicate in unit test so we use mocks to simulate the behavior of these real objects.
(not covered in this script)
'''


'''
What are fixtures?
TLDR; in real-world application, you may have 5-10 lines of setup code for every test you run.
(i.e. you may need to intialize a connection to a database, or create a user, etc. before you test each class method)

Thus, Fixtures can be used to simplify this setup code. Fixtures are functions that run before each test method to which it is applied. (you apply fixtures by passing them as arguments to any test method)

In this case, of course we're simply initializing a simple cart object, but in the real world you'd have more complex setup code.
'''
@pytest.fixture
def cart():
    # All setup code can be placed here...
    return ShoppingCart(max_size=3)

# each unit test is a function (need to have the word test in your unit test)
# this test checks if we can successfully add item to cart
def test_can_add_item_to_cart(cart):
    '''
    This test checks if we can successfully add item to cart
    '''
    # old code=> you used to need to instantiate a new cart object everytime you run a test, but with fixtures, you don't need to anymore.
    # cart = ShoppingCart(max_size=3)
    cart.add("apple")
    # Using code, how can you check that the item was added to the cart successfully?
    # In the ShoppingCart class, you have some methods to do so, i.e. using the size method to see number of items in cart

    # we use the 'assert' to check if this statement is true; if it's not, then the test will fail
    # TLDR; u need cart size == 1 for this to pass
    assert cart.size() == 1


def test_cart_contains_added_item(cart):
    '''
    This test checks if the cart contains the added item, i.e. apple
    '''
    cart.add("apple")
    assert "apple" in cart.get_items()



def test_cart_exceed_max_items_should_fail(cart):
    '''
    This test is to ensure that the cart cannot add more than the max number of items allowed
    (i.e. it should fail if we try to add more than the max number of items; this test case can only "pass" if we fail to add more than the max number of items - if you get me)
    '''
    # add 3 items
    cart.add("apple")
    cart.add("banana")
    cart.add("orange")
    # this code checks that whenever we run the test logic below, we are expecting this specific "OverflowError" error; everytime the error raised is NOT OverflowError, or if there are no errors raised at all, then the test will fail

    # in your ShoppingCart class, you should add the logic to raise this overflow error (i.e. you do a check for current item size and if it exceeds max cart size, you raise the overflow error. In this test class, you're merely ensuring that this is INDEED raised when the user tries to add more items than max cart size allowed)
    with pytest.raises(OverflowError):
        # test logic (add final item which should lead to overflow)
        cart.add("pear")
    


def test_can_get_total_price():
    cart = ShoppingCart(max_size=3)
    cart.add("apple")
    cart.add("banana")

    price_map = {
        "apple": 1.0,
        "banana": 1.50
    }
    assert cart.get_total_price(price_map) == 2.50
    
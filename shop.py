####################### DO NOT MODIFY THIS CODE ########################

menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################


cupcake_shop_name = "Tuwake"
signature_flavors = ["tuna","salmon","red herring"]
order_list = []




def print_menu():
    print ("Our menu:")
    for item in menu:
        print (item + " (KD " + str(menu[item]) + ")")


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for item in original_flavors:
        print (item)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for item in signature_flavors:
        print (item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    valid = False
    if order in menu:
        valid = True
        
    if order in original_flavors:
        valid = True
        
    if order in signature_flavors:
        valid = True
        
    return valid



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    # your code goes here!
    print ("What is your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order)")
    exit = True
    while exit:
        text = input("")

        if text != 'Exit':
            check = is_valid_order(text)
            if check:
                order_list.append(text)
                print ("Your order is exists, What else would you like? ")
            else:
                print ("Your order not exists , Please enter again:")
        else:
            exit = False
            break
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    return True if total > 5 else False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if order in menu:
            total += menu[order]
        elif order in original_flavors:
            total += original_price
        else:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for order in order_list:
        print (order)

    total = get_total_price(order_list)
    print ("Your total is %s SR:" %(total))
    if accept_credit_card(total):
        print("You can pay by credit or cash")
    else:
        print("You can pay by only cash")

    print ("Thank you for using %s " %(cupcake_shop_name))

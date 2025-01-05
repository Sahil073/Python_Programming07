
availabelItmes = {
    1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5},
    2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35},
    3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
    4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
    5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}
}

def things_finder(item):
    for key, value in availabelItmes.items():
        if value['Item'] == item:
            isPresent = True
            particular_quantity = value['Quantity']
            particular_cost = value['Cost/Item']
            return [isPresent, particular_quantity, particular_cost]
    return [False, 0, 0]

def display_shopping_cart(cart):
    print("Welcome to Ram Library".center(100))
    print(f'{"S.No":<15}{"Item":<15}{"Quantity":<15}')
    for i, (item, details) in enumerate(cart.items(), 1):
        print(f'{i:<15}{item:<15}{details["quantity"]:<15}')

def add_item_inCart(user_cart):
    item_to_added = input("Enter item name to add: ")
    number_quantity = int(input('Enter Number of quantity: '))
    present, quan, costt = things_finder(item_to_added)
    if present:
        if item_to_added in user_cart:
            user_cart[item_to_added]['quantity'] += number_quantity
        else:
            user_cart[item_to_added] = {'quantity': number_quantity}
        print(f'{number_quantity} of {item_to_added} added to cart.')
    else:
        print(f'{item_to_added} is Not Available Right Now, You Will be notified SOON')    

def remove_item_inCart(user_cart):
    item_to_added = input("Enter item name to remove: ")
    number_quantity = int(input("Enter number of quantity: "))
    
    if item_to_added in user_cart:
        if number_quantity >= user_cart[item_to_added]['quantity']:
            del user_cart[item_to_added]
            print(f"All {item_to_added}s removed from the cart.")
        else:
            user_cart[item_to_added]['quantity'] -= number_quantity
            print(f"{number_quantity} {item_to_added}(s) removed, {user_cart[item_to_added]['quantity']} left in the cart.")
    else:
        print("Item not found in cart")

def replace_item_inCart(user_cart):
    item_to_replace = input("Enter item name to replace: ")
    item_to_add = input("Enter the name of item to add: ")
    number_quantity = int(input('Enter Number of quantity: '))
    
    if item_to_replace in user_cart:
        user_cart[item_to_add] = {'quantity': number_quantity}
        del user_cart[item_to_replace]
        print(f"{item_to_replace} replaced with {item_to_add} ({number_quantity}) in cart.")
    else:
        print("No such item in cart.")

user_cart = {}
while True:
    user_said = input("What do you want to perform: ")
    match user_said:
        case "add to cart":
            add_item_inCart(user_cart)
        case "remove from cart":
            remove_item_inCart(user_cart)
        case "replace item in cart":
            replace_item_inCart(user_cart)
        case "display my cart":
            display_shopping_cart(user_cart)
        case "no more item":
            print("Have a good day!")
            break

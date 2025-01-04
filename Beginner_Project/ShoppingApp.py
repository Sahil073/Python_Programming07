
availabelItmes = {
    1:{'Item': 'Biscuits', 'Quantity':5, 'Cost/Item':20.5},
    2:{'Item': 'Chocolates', 'Quantity':10, 'Cost/Item':35},
    3:{'Item': 'Coffee', 'Quantity':25, 'Cost/Item':55},
    4:{'Item': 'Chips', 'Quantity':10, 'Cost/Item':50},
    5:{'Item': 'Cream', 'Quantity':5, 'Cost/Item':30}
}

def display_shopping_cart(dict):
    print("Welcome to Ram Library".center(100))
    print(f'{'S.No':<15}{'Item':<15}{'Quantity':<15}{'Cost/Item':<15}')
    for sno, values in dict.items():
        print(f'{sno:<15}{values['Item']:<15}{values['Quantity']:<15}{values['Cost/Item']:<15}')  
def add_item_inCart(user_cart):
    item_to_added = input("Enter item name to add: ")
    number_quantity = int(input('Enter Number of quantity: '))
    user_cart[item_to_added] = number_quantity
    print("Item added succesfully")
def remove_item_inCart(user_cart):
    item_to_added = input("Enter item name to remove: ")
    number_quantity = int(input('Enter Number of quantity: '))
    if number_quantity == 0:
        del user_cart[item_to_added]
    else:    
        user_cart[item_to_added] = number_quantity
def replace_item_inCart(user_cart):
    item_to_added = input("Enter item name: ")
    number_quantity = int(input('Enter Number of quantity: '))
    user_cart[item_to_added] = number_quantity
    


while True:
    user_said = input("wht you want to perfrom")
    user_cart = {}
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
            print("Have a good day")
            break        

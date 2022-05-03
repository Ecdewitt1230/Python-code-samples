# Colton DeWitt - May 3, 2022
class ItemToPurchase:
    def __init__(self, item_name='none', item_description='none',
                 item_price=0, item_quantity=0):  # Initialize and sets defaults of item to buy
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_description(self):  # Print the item description
        print('{}: {}'.format(self.item_name, self.item_description))

    def print_item_cost(self):  # Calculates total cost of items and prints it
        total_cost = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, total_cost))
        #return total_cost

class ShoppingCart:  # Customer's shopping cart
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, item):  # Adds an item to customer's cart
        self.cart_items.append(item)

    def remove_item(self, removing_item):  # Remove an item from customer's cart
        item_removed = False
        for item in self.cart_items:  # Iterate through the customer's cart
            if removing_item == item.item_name:  # Search each class object in cart and check the name
                self.cart_items.remove(item)  # Remove the class object with the matching name of item to remove
                print()
                item_removed = True

        if item_removed == False:
            print('Item not found in cart. Nothing removed.\n')

    def modify_item(self, changing_item, changed_quantity):
        item_changed = False
        for item in self.cart_items:
            if changing_item == item.item_name:  # Search each class object in cart and check the name
                item.item_quantity = changed_quantity  # Update the quantity attribute of the correct instance object
                item_changed = True

        if item_changed == False:
            print('Item not found in cart. Nothing modified.\n')

    def get_num_items_in_cart(self):
        num_items_in_cart = 0
        for item in self.cart_items:  # Iterate through the cart
            num_items_in_cart += item.item_quantity  # Check each instances quantity attribute and add to num_items_in_c
        return num_items_in_cart  # Quantity of items in the cart

    def get_cost_of_cart(self):
        total_cost_cart = 0
        for item in self.cart_items:  # TODO Validate if cart is empty???
            total_cost_cart += item.item_price * item.item_quantity  # For example, three $1 water bottle: 1 * 3 bottles
        return total_cost_cart

    def print_total(self):  # Print the user's shopping cart and items in it, with their prices. Also total price at end
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        if self.get_num_items_in_cart() == 0:
            print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))  # In this case prints 0 items
            print('SHOPPING CART IS EMPTY')
        else:
            print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))  # Print quantity of items
            for item in self.cart_items:  # Iterate though the shopping cart
                item.print_item_cost()  # Print each item in cart and its cost

        print('\nTotal: ${}\n'.format(self.get_cost_of_cart()))  # Print total cost of all items in cart

    def print_descriptions(self):  # Print the user's shopping cart and each item's description. No prices
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('\nItem Descriptions')
        for item in self.cart_items:
            item.print_item_description()
        print()


def print_menu():  # Print to the user the main menu and their available options
    #valid_options = ['a', 'r', 'c', 'i', 'o', 'q']
    print('MENU\n'
          'a - Add item to cart\n'
          'r - Remove item from cart\n'
          'c - Change item quantity\n'
          'i - Output items\' descriptions\n'
          'o - Output shopping cart\n'
          'q - Quit')
    #user_choice = input('\nChoose an option:\n')
    #while user_choice not in valid_options:
        #print('Invalid choice. Please try again')
        #user_choice = input('\nChoose an option:\n')

    #return user_choice


def execute_menu(user_choice, shopping_cart):  # Get's the user's choice of action from main and the current shop cart

    if user_choice == 'a':
        print('ADD ITEM TO CART')
        new_item = ItemToPurchase(input('Enter the item name:\n'), input('Enter the item description:\n'),
                                  int(input('Enter the item price:\n')), int(input('Enter the item quantity:\n')))
        shopping_cart.add_item(new_item)
        print()
    elif user_choice == 'r':
        print('REMOVE ITEM FROM CART')
        item_to_remove = input('Enter name of item to remove:\n')
        shopping_cart.remove_item(item_to_remove)
    elif user_choice == 'c':
        print('CHANGE ITEM QUANTITY')
        item_to_change = input('Enter the item name:\n')
        new_quantity = int(input('Enter the new quantity:\n'))
        shopping_cart.modify_item(item_to_change, new_quantity)
    elif user_choice == 'i':
        print('OUTPUT ITEMS\' DESCRIPTIONS')  # Print the user's shopping cart and each item's description. No prices
        shopping_cart.print_descriptions()
    elif user_choice == 'o':
        print('OUTPUT SHOPPING CART')  # Shopping cart items and their prices, plus total price of cart
        shopping_cart.print_total()


if __name__ == '__main__':
    customer_cart1 = ShoppingCart(input('Enter customer\'s name:\n'), input('Enter today\'s date:\n'))
    print('\nCustomer name: {}\nToday\'s date: {}\n'.format(customer_cart1.customer_name, customer_cart1.current_date))

    valid_options = ['a', 'r', 'c', 'i', 'o', 'q']
    user_choice_option = 'none'
    while user_choice_option != 'q':  # Will loop until the user quits the program with 'q'
        print_menu()
        user_choice_option = 'none'
        while user_choice_option not in valid_options:
            # print('Invalid choice. Please try again')
            user_choice_option = input('\nChoose an option:')  # Get user choice here, must be in valid_options list ^
        print()
        execute_menu(user_choice_option, customer_cart1)
        #if user_choice_option != 'q':
            #execute_menu(customer_cart1)

    print('User exited the program. Have a nice day.')  # Will print after user input 'q', while loop ended

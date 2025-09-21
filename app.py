## Import required packaged
import os
import time

## Sample data for products
categories = ["Sports","Electronics","Furniture"]
items = [["Yonex Badminton Racquet","Felet Badminton Racquet","Nike Runner Shoes Mark II","Puma Jogging Socks"],
         ["iPhone 17 Pro Max 256GB","iPhone Air","Airpods Pro 3","Samsung Z Fold 7 1TB"],
         ["Ikea Essential Chair","3A Plastic Chair","Foldable Table"]]
quantity = [[59,65,90,30],
            [200,582,569,223],
            [477,896,452]]
price = [[200,250,500,90],
         [5999,4999,999,9999],
         [59,120,299]]
reviews = [
    [4.5, 4.2, 4.8, 3.9],
    [4.7, 4.3, 4.6, 4.4],
    [3.8, 3.5, 4.1]
]

# Shopping cart dictionary to store items {(category_index, item_index): quantity}
shopping_cart = {}

def get_valid_integer(prompt, min_val=None, max_val=None):
    """Get a valid integer input from user with range validation"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Please enter a number larger than {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a number smaller than {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_yes_no_input(prompt):
    """Get a valid yes/no input from user"""
    while True:
        response = input(prompt).lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def clear_screen():
    """Clear screen in a cross-platform way"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_products(cat_index):
    """Display products"""
    print(f"\n=== {categories[cat_index]} ===")
    
    print("-" * 70)
    print(f"{'No.':<3} {'Product':<30} {'Price':<8} {'Stock':<7} {'Rating':<7}")
    print("-" * 70)
    
    for i in range(len(items[cat_index])):
        name = items[cat_index][i]
        item_price = price[cat_index][i]
        stock = quantity[cat_index][i]
        rating = reviews[cat_index][i]
        print(f"{i + 1:<3} {name:<30} ${item_price:<7} {stock:<7} {rating:<7}")
    print("-" * 70)

def add_to_cart(cat_index, item_index, qty):
    """Add item to shopping cart"""
    cart_key = (cat_index, item_index)
    if cart_key in shopping_cart:
        shopping_cart[cart_key] += qty
    else:
        shopping_cart[cart_key] = qty
    
    # Update inventory
    quantity[cat_index][item_index] -= qty
    print(f"Added {qty} x {items[cat_index][item_index]} to cart!")


def edit_cart():
    """Edit items in shopping cart - modify quantity or remove"""
    if not shopping_cart:
        print("Your cart is empty!")
        return
    
    print("\n=== Edit Cart ===")
    display_cart_items()
    
    # Get valid item selection
    max_items = len(shopping_cart)
    choice = get_valid_integer(f"Enter item number to edit (1-{max_items}), 0 to cancel: ", 0, max_items)
    
    if choice == 0:
        return
    
    cart_items = list(shopping_cart.items())
    cart_key, current_qty = cart_items[choice - 1]
    cat_index, item_index = cart_key
    item_name = items[cat_index][item_index]
    
    print(f"\nSelected: {item_name}")
    print(f"Current quantity in cart: {current_qty}")
    print(f"Available stock: {quantity[cat_index][item_index]}")
    
    print("\nOptions:")
    print("1. Update quantity")
    print("2. Remove item completely")
    print("3. Cancel")
    
    edit_choice = get_valid_integer("Choose option (1-3): ", 1, 3)
    
    if edit_choice == 1:
        # Update quantity
        max_available = quantity[cat_index][item_index] + current_qty  # Current cart qty + available stock
        print(f"Enter new quantity (current: {current_qty}, max available: {max_available})")
        new_qty = get_valid_integer("New quantity: ", 1, max_available)
        
        # Calculate the difference
        qty_difference = new_qty - current_qty
        
        if qty_difference > 0:
            # Adding more items
            shopping_cart[cart_key] = new_qty
            quantity[cat_index][item_index] -= qty_difference
            print(f"Updated quantity to {new_qty}")
            
        elif qty_difference < 0:
            # Removing some items - return to inventory
            shopping_cart[cart_key] = new_qty
            quantity[cat_index][item_index] += abs(qty_difference)
            print(f"Updated quantity to {new_qty}")
            
        else:
            print("Quantity unchanged.")
    
    elif edit_choice == 2:
        # Remove item completely
        if get_yes_no_input(f"Are you sure you want to remove {item_name}? (y/n): "):
            # Return all items to inventory
            quantity[cat_index][item_index] += current_qty
            # Remove from cart
            del shopping_cart[cart_key]
            print(f"Removed {item_name} from cart!")
        else:
            print("Removal cancelled.")
    
    elif edit_choice == 3:
        print("Edit cancelled.")

def display_cart_items():
    """Display items in cart with numbering"""
    if not shopping_cart:
        print("Your cart is empty!")
        time.sleep(3)
        return
    
    print("-" * 60)
    print(f"{'No.':<3} {'Product':<25} {'Price':<8} {'Qty':<5} {'Total':<8}")
    print("-" * 60)
    
    for idx, (cart_key, cart_qty) in enumerate(shopping_cart.items(), 1):
        cat_index, item_index = cart_key
        item_name = items[cat_index][item_index]
        item_price = price[cat_index][item_index]
        total_price = item_price * cart_qty
        print(f"{idx:<3} {item_name:<25} ${item_price:<7} {cart_qty:<5} ${total_price:<7}")

def display_cart_summary():
    """Display cart summary with total"""
    if not shopping_cart:
        print("Your cart is empty!")
        return 0
    
    print("\n=== Shopping Cart Summary ===")
    display_cart_items()
    
    total_items = sum(shopping_cart.values())
    total_price = sum(price[cat_index][item_index] * cart_qty 
                     for (cat_index, item_index), cart_qty in shopping_cart.items())
    
    print("-" * 60)
    print(f"Total Items: {total_items}")
    print(f"Total Price: ${total_price}")
    print("-" * 60)
    
    return total_price

def main_menu():
    """Display main menu and handle user choices"""
    while True:
        clear_screen()
        print("\n=== Mini Online Shop ===")
        print("1. Browse Sports")
        print("2. Browse Electronics") 
        print("3. Browse Furniture")
        print("4. View Cart")
        print("5. Edit Cart")
        print("6. Checkout")
        print("7. Exit")
        
        choice = get_valid_integer("Enter your choice (1-7): ", 1, 7)
        
        if choice in [1, 2, 3]:
            clear_screen()
            cat_index = choice - 1
            
            display_products(cat_index)
            
            # Product selection with validation
            max_products = len(items[cat_index])
            product_choice = get_valid_integer(f"Select product (1-{max_products}), 0 to go back: ", 0, max_products)
            
            if product_choice == 0:
                continue
            
            clear_screen()
            item_index = product_choice - 1
            
            # Show product details
            print(f"\nProduct: {items[cat_index][item_index]}")
            print(f"Price: ${price[cat_index][item_index]}")
            print(f"Rating: {reviews[cat_index][item_index]}/5")
            print(f"Available: {quantity[cat_index][item_index]} units")
            
            # Quantity input with validation
            max_qty = quantity[cat_index][item_index]
            if max_qty == 0:
                print("Sorry, this item is out of stock!")
                input("Press Enter to continue...")
                continue
            
            qty = get_valid_integer(f"Enter quantity (1-{max_qty}): ", 1, max_qty)
            
            # Add to cart
            add_to_cart(cat_index, item_index, qty)
            input("\nPress Enter to continue...")
        
        elif choice == 4:
            clear_screen()
            display_cart_summary()
            input("\nPress Enter to continue...")
        
        elif choice == 5:
            clear_screen()
            edit_cart()
            input("\nPress Enter to continue...")
        
        elif choice == 6:
            clear_screen()
            if not shopping_cart:
                print("Your cart is empty!")
                input("Press Enter to continue...")
                continue
            
            total_price = display_cart_summary()
            
            if get_yes_no_input("\nDo you want to proceed with the purchase? (y/n): "):
                clear_screen()
                shopping_cart.clear()
                print(f"\nThank you for your purchase of ${total_price}!")
                print("Your order has been confirmed!")
                input("Press Enter to continue...")
            else:
                print("Purchase cancelled. Items remain in your cart.")
                input("Press Enter to continue...")
        
        elif choice == 7:
            clear_screen()
            if shopping_cart:
                print("\nYou have items in your cart:")
                display_cart_summary()
                print("Thank you for visiting!")
            else:
                print("Thank you for visiting!")
            break

# Start the application
if __name__ == "__main__":
    main_menu()
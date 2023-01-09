# Vending machine program

# List of products available in the vending machine
# Each product is a dictionary with keys for the name, code, price, and quantity
products = [
    
    {"name": "Dew", "code": "A1", "price": 1.50, "quantity": 8},
    
    {"name": "Lays Chips", "code": "A2", "price": 1.50, "quantity": 20},
    
    {"name": "Kitkat", "code": "A3", "price": 1.50, "quantity": 20},
    
    {"name": "Oman Chips", "code": "A4", "price": 1.50, "quantity": 20},
    
    {"name": "Dairy Milk", "code": "B1", "price": 0.75, "quantity": 8},
    
    {"name": "Takkis", "code": "B2", "price": 0.75, "quantity": 5},
    
    {"name": "Pran Juice", "code": "B3", "price": 0.75, "quantity": 20},
    
    {"name": "Barbican", "code": "B4", "price": 0.75, "quantity": 10},
]

# Function to display the menu
# This function simply prints a list of products and their codes
def display_menu():
    print("\n""Welcome to the Vending Machine!""\n")
    
    print("\n""Here is a list of products available:""\n")
    
    for product in products:
        print(f"{product['code']}: {product['name']} - ${product['price']:.2f}")

# Function to process the purchase
# This function takes the code of the product and the amount paid as arguments
# It checks if the entered code is valid, if there is sufficient quantity of the product,
# and if the amount paid is sufficient. If all these conditions are met, it dispenses
# the product and calculates the change. Otherwise, it prints an appropriate error message.
def process_purchase(code, amount_paid):
    # Search for the product with the entered code
    for product in products:
        if product['code'] == code:
            # Check if there is sufficient quantity of the product
            if product['quantity'] > 0:
                # Check if the amount paid is sufficient
                if product['price'] <= amount_paid:
                    # Dispense the product and calculate the change
                    product['quantity'] -= 1
                    change = amount_paid - product['price']
                    print("\n"f"Enjoy your {product['name']}! Your change is ${change:.2f}.""\n")
                else:
                    print("\n""Insufficient payment. Please enter more money.""\n")
            else:
                print("Sorry, this product is currently out of stock.")
            return
    # If the code is invalid, print an error message
    print("Invalid product code. Please try again.")

# Main program loop
# This loop repeatedly displays the menu, prompts the user to enter a code and an amount of money,
# and processes the purchase. The loop exits when the user enters the code "exit".
while True:
    display_menu()
    code = input("Enter the code of the product you want to purchase: ")
    if code == "exit":
        break
    amount_paid = float(input("Enter the amount of money you are inserting: "))
    process_purchase(code, amount_paid)
   

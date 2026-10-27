names = ["Wireless Mouse", "USB Keyboard", "Laptop Stand", "HD Webcam", "USB-C Hub"]
prices = [599.0, 899.0, 1499.0, 2199.0, 1299.0]
stocks = [10, 5, 3, 4, 8]

cart = []  # (product_index, quantity)

# Display products
print("\n--- Available Products ---")
for i in range(len(names)):
    print(f"{i + 1}. {names[i]:<16} ₹{prices[i]:>8.2f}  Stock: {stocks[i]}")

# Search products
keyword = input("\nSearch: ").strip().lower()
matches = 0

for i in range(len(names)):
    if keyword in names[i].lower():
        print(f"{names[i]:<16} ₹{prices[i]:>8.2f}  Stock: {stocks[i]}")
        matches += 1

if matches == 0:
    print(f"No products match '{keyword}'.")

# Add products to cart
while True:
    choice = input("\nEnter product number to add (or 0 to checkout): ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        continue

    i = int(choice) - 1

    if i == -1:
        break

    if i < 0 or i >= len(names):
        print("Invalid product number.")
        continue

    qty_input = input("Enter quantity: ")

    if not qty_input.isdigit() or int(qty_input) <= 0:
        print("Quantity must be a positive integer.")
        continue

    qty = int(qty_input)

    if qty > stocks[i]:
        print(f"Only {stocks[i]} units available.")
        continue

    cart.append((i, qty))
    stocks[i] -= qty
    print(f"Added {qty} x {names[i]} to cart.")

# Display cart and calculate subtotal
print("\n--- Your Cart ---")
subtotal = 0

for i, qty in cart:
    item_total = prices[i] * qty
    subtotal += item_total
    print(f"{names[i]:<16} x {qty} = ₹{item_total:.2f}")

if not cart:
    print("Your cart is empty.")

# Apply discount
rate = (
    0.10 if subtotal > 5000
    else 0.05 if subtotal > 1000
    else 0.0
)

discount = subtotal * rate
total = subtotal - discount

# Display bill
print("\n--- Bill Summary ---")
print(f"Subtotal:  ₹{subtotal:.2f}")
print(f"Discount:  ₹{discount:.2f} ({rate:.0%})")
print(f"Total:     ₹{total:.2f}")
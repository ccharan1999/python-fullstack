STORE_NAME = "ShopEase"
GST_RATE = 0.18
 
# Three products as separate variables (lists come on Day 3)
p1_name, p1_price, p1_stock = "Wireless Mouse", 599.0, 10
p2_name, p2_price, p2_stock = "USB Keyboard", 899.0, 5
p3_name, p3_price, p3_stock = "Laptop Stand", 1499.0, 3
 
# Cart: quantity of each product
q1 = q2 = q3 = 0
 
print(f"{'=' * 36}\n{STORE_NAME:^36}\n{'=' * 36}")
 
while True:
    print("\n1. View products  2. Add to cart  3. Checkout  4. Exit")
    choice = input("Choose an option: ").strip()
 
    if choice == "1":
        print(f"{'No':<4}{'Product':<16}{'Price':>9}{'Stock':>7}")
        print(f"{1:<4}{p1_name:<16}{p1_price:>9.2f}{p1_stock:>7}")
        print(f"{2:<4}{p2_name:<16}{p2_price:>9.2f}{p2_stock:>7}")
        print(f"{3:<4}{p3_name:<16}{p3_price:>9.2f}{p3_stock:>7}")
    elif choice == "2":
        no = input("Product number (1-3): ").strip()
        qty_text = input("Quantity: ").strip()
        if not qty_text.isdigit() or int(qty_text) == 0:
            print("Please enter a whole number greater than 0.")
            continue
        qty = int(qty_text)
 
        if no == "1" and qty <= p1_stock:
            q1 += qty
            p1_stock -= qty
            print(f"Added {qty} x {p1_name}")
        elif no == "2" and qty <= p2_stock:
            q2 += qty
            p2_stock -= qty
            print(f"Added {qty} x {p2_name}")
        elif no == "3" and qty <= p3_stock:
            q3 += qty
            p3_stock -= qty
            print(f"Added {qty} x {p3_name}")
        elif no in ("1", "2", "3"):
            print("Sorry, not enough stock.")
        else:
            print("Invalid product number.")
            
    elif choice == "3":
        subtotal = q1 * p1_price + q2 * p2_price + q3 * p3_price
        if subtotal == 0:
            print("Your cart is empty.")
            continue
 
        # Discount slabs
        if subtotal > 5000:
            rate = 0.10
        elif subtotal > 1000:
            rate = 0.05
        else:
            rate = 0.0
 
        discount = subtotal * rate
        gst = (subtotal - discount) * GST_RATE
        total = subtotal - discount + gst
 
        print(f"{'Subtotal':<18}Rs {subtotal:>10,.2f}")
        print(f"{f'Discount ({rate:.0%})':<18}Rs {discount:>10,.2f}")
        print(f"{'GST (18%)':<18}Rs {gst:>10,.2f}")
        print(f"{'TOTAL':<18}Rs {total:>10,.2f}")
        print("Thank you for shopping with ShopEase!")
        continue
    elif choice == "4":
        print("Goodbye!")
        break
 
    else:
        print("Invalid choice, try again.")


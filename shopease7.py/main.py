"""main.py — ShopEase Day 7: data saved to files, errors handled."""
import storage
from errors import ShopError, ProductNotFoundError
from models import Customer, Cart, Order
 
MENU = ("1. View  2. Search  3. Add  4. Remove  5. Cart\n"
        "6. Checkout  7. Order history  8. Export CSV  9. Exit")
 
 
def read_int(prompt):
    """Ask until the user types a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
 
 
def find(products, pid):
    for p in products:
        if p.pid == pid:
            return p
        raise ProductNotFoundError(f"No product with ID {pid}")
 
 
def print_table(items):
    print(f"{'ID':<5}{'Product':<16}{'Category':<13}{'Price':>9}{'Stock':>7}")
    for p in items:
        print(p)
 
 
def main():
    products = storage.load_products()
    Order.continue_numbering(len(storage.load_orders()))
    print(f"{'=' * 50}\n{'ShopEase':^50}\n{'=' * 50}")
    customer = Customer(input("Your name: "), input("Your email: "))
    cart = Cart()
 
    while True:
        print("\n" + MENU)
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                print_table(products)
            elif choice == "2":
                word = input("Search: ").strip().lower()
                found = [p for p in products if word in p.name.lower()]
                if found:
                    print_table(found)
                else:
                    print("No matches.")
            elif choice == "3":
                product = find(products, read_int("Product ID: "))
                qty = read_int("Quantity: ")
                cart.add(product, qty)
                print(f"Added {qty} x {product.name}")
            elif choice == "4":
                product = find(products, read_int("Product ID to remove: "))
                removed = cart.remove(product)
                print(f"Removed {removed} item(s)." if removed else "Not in cart.")
            elif choice == "5":
                if not cart:
                    print("Your cart is empty.")
                for product, qty, total in cart.lines():
                    print(f"{product.name:<16} x {qty:<3} Rs {total:>9,.2f}")
            elif choice == "6":
                if not cart:
                    print("Your cart is empty.")
                    continue
                order = Order(customer, cart)
                storage.save_order(order)
                storage.save_products(products)      # remember the new stock
                print(order.receipt())
                print(f"Order saved. Thank you, {customer.name}!")
                break
            elif choice == "7":
                orders = storage.load_orders()
                if not orders:
                    print("No orders yet.")
                for o in orders:
                    print(f"{o['number']}  {o['date']}  {o['customer']:<10}"
                          f"Rs {o['total']:>10,.2f}")
            elif choice == "8":
                count = storage.export_orders_csv("orders_export.csv")
                print(f"Exported {count} order(s) to orders_export.csv")
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        except ShopError as error:            # any ShopEase problem
            print("Sorry:", error)
 
 
if __name__ == "__main__":
    main()

import products
from cart import add_item, remove_item, cart_lines
from billing import calculate_bill, print_bill
def main():
    cart = {}
    while True:
        choice = input("Choose an option: ").strip()
        if choice == "1":
            products.print_table(products.PRODUCTS)
        elif choice == "2":
            found = products.search(input("Search: "))
            ...
        elif choice == "4":
            pid = read_int("Product ID: ")
            qty = read_int("Quantity: ")
            ok, message = add_item(cart, pid, qty)
            print(message)
        elif choice == "7":
            print_bill(calculate_bill(cart))
            break
if __name__ == "__main__":
    main()
def read_int(prompt):
    while True:
        text = input(prompt).strip()
        if text.isdigit():
            return int(text)
        print("Please enter a whole number.")
def show_cart(cart):
    lines = cart_lines(cart)
    if not lines:
        print("Your cart is empty.")
    for name, qty, total in lines:
        print(f"{name:<16} x {qty:<3}"
              f"Rs {total:>9,.2f}")
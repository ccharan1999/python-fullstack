
"""main.py — ShopEase Day 6: the menu, now working with objects."""

import catalog
from models import Customer, Cart, Order


MENU = (
    "1. View  2. Search  3. Add  4. Remove\n"
    "5. Cart  6. Checkout  7. Exit"
)


def read_int(prompt):
    while True:
        text = input(prompt).strip()

        if text.isdigit():
            return int(text)

        print("Please enter a whole number.")


def main():
    print(f"{'=' * 50}\n{'ShopEase':^50}\n{'=' * 50}")

    customer = Customer(
        input("Your name: "),
        input("Your email: ")
    )

    cart = Cart()

    print(f"Welcome, {customer.name}!")

    while True:
        print("\n" + MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            catalog.print_table(catalog.PRODUCTS)

        elif choice == "2":
            found = catalog.search(input("Search: "))

            if found:
                catalog.print_table(found)
            else:
                print("No matches.")

        elif choice == "3":
            product = catalog.find(read_int("Product ID: "))

            if product is None:
                print("Unknown product ID.")
                continue

            qty = read_int("Quantity: ")

            try:
                cart.add(product, qty)
                print(f"Added {qty} x {product.name}")
            except ValueError as error:
                print(error)

        elif choice == "4":
            product = catalog.find(
                read_int("Product ID to remove: ")
            )

            removed = cart.remove(product) if product else 0

            if removed:
                print(f"Removed {removed} item(s).")
            else:
                print("Not in cart.")

        elif choice == "5":
            if not cart:
                print("Your cart is empty.")
            else:
                for product, qty, total in cart.lines():
                    print(
                        f"{product.name:<16} "
                        f"x {qty:<3} "
                        f"Rs {total:>9,.2f}"
                    )

        elif choice == "6":
            if not cart:
                print("Your cart is empty.")
                continue

            order = Order(customer, cart)
            print(order.receipt())

            count = len(customer.orders)
            print(
                f"Thank you, {customer.name}! "
                f"Orders placed: {count}"
            )
            break

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

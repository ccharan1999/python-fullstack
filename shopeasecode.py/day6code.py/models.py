
from datetime import date


class Product:
    """A physical product that has stock and attracts GST."""

    GST_RATE = 0.18  # Class attribute: shared by all products

    def __init__(self, pid, name, price, category, stock=0):
        self.pid = pid
        self.name = name
        self.price = price  # Goes through the property setter
        self.category = category
        self._stock = stock  # Change it through methods

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")

        self._price = float(value)

    @property
    def stock(self):
        return self._stock

    def in_stock(self, qty=1):
        return self._stock >= qty

    def reduce_stock(self, qty):
        if not self.in_stock(qty):
            raise ValueError(f"Only {self._stock} {self.name} left")

        self._stock -= qty

    def restock(self, qty):
        self._stock += qty

    def price_with_gst(self):
        return round(self.price * (1 + self.GST_RATE), 2)

    def __str__(self):
        return (
            f"{self.pid:<5}{self.name:<16}{self.category:<13}"
            f"{self.price:>9.2f}{self.stock:>7}"
        )

    def __repr__(self):
        return f"Product({self.pid}, {self.name!r}, {self.price})"


class DigitalProduct(Product):
    """A downloadable product: unlimited stock, no GST in this example."""

    GST_RATE = 0.0  # Overrides the parent's class attribute

    def __init__(self, pid, name, price, category, download_url):
        super().__init__(pid, name, price, category, stock=0)
        self.download_url = download_url

    def in_stock(self, qty=1):
        # Polymorphism: same method, new behaviour
        return True

    def reduce_stock(self, qty):
        pass  # Nothing to reduce for a download

    def __str__(self):
        return (
            f"{self.pid:<5}{self.name:<16}{self.category:<13}"
            f"{self.price:>9.2f}{'online':>7}"
        )


class Customer:
    """A shopper with a name, email and order history."""

    def __init__(self, name, email):
        self.name = name.strip().title()
        self.email = email.strip().lower()
        self.orders = []

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Cart:
    """Holds products and quantities for one customer."""

    def __init__(self):
        self._items = {}  # Product -> quantity

    def add(self, product, qty=1):
        if qty <= 0:
            raise ValueError("Quantity must be at least 1")

        product.reduce_stock(qty)
        self._items[product] = self._items.get(product, 0) + qty

    def remove(self, product):
        qty = self._items.pop(product, 0)

        if qty:
            product.restock(qty)

        return qty

    def lines(self):
        return [
            (p, q, p.price * q)
            for p, q in self._items.items()
        ]

    def subtotal(self):
        return sum(total for _, _, total in self.lines())

    def gst(self, discount_rate=0.0):
        return sum(
            p.price * q * (1 - discount_rate) * p.GST_RATE
            for p, q in self._items.items()
        )

    def clear(self):
        self._items.clear()

    def __len__(self):
        # len(cart) -> number of units
        return sum(self._items.values())

    def __bool__(self):
        # if cart: ...
        return bool(self._items)


class Order:
    """A confirmed purchase with a bill that can no longer change."""

    _next_number = 1  # Class attribute used as a counter

    def __init__(self, customer, cart):
        self.number = f"SE{Order._next_number:05d}"
        Order._next_number += 1

        self.customer = customer
        self.date = date.today()
        self.lines = cart.lines()
        self.subtotal = cart.subtotal()
        self.rate = self.discount_rate(self.subtotal)
        self.discount = self.subtotal * self.rate
        self.gst = cart.gst(self.rate)
        self.total = self.subtotal - self.discount + self.gst

        customer.orders.append(self)

    @staticmethod
    def discount_rate(subtotal):
        """10% above Rs 5,000, 5% above Rs 1,000, otherwise none."""

        if subtotal > 5000:
            return 0.10

        if subtotal > 1000:
            return 0.05

        return 0.0

    def receipt(self):
        rows = [
            f"Order {self.number} · {self.customer.name}",
            "-" * 40
        ]

        for product, qty, total in self.lines:
            rows.append(
                f"{product.name:<16} x {qty:<3} Rs {total:>10,.2f}"
            )

        rows.append("-" * 40)
        rows.append(
            f"{'Subtotal':<20} Rs {self.subtotal:>10,.2f}"
        )

        label = f"Discount ({self.rate:.0%})"
        rows.append(
            f"{label:<20} Rs {self.discount:>10,.2f}"
        )

        rows.append(f"{'GST':<20} Rs {self.gst:>10,.2f}")
        rows.append(f"{'TOTAL':<20} Rs {self.total:>10,.2f}")

        return "\n".join(rows)

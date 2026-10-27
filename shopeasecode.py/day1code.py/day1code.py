STORE_NAME = "ShopEase"
TAGLINE = "Smart shopping, simple prices"
GST_RATE = 0.18
 
print("=" * 40)
print(f"{STORE_NAME:^40}")
print(f"{TAGLINE:^40}")
print("=" * 40)
 
customer = input("Your name: ").strip().title()
print(f"\nWelcome, {customer}! Today's featured product:")
 
product = "Wireless Mouse"
price = 599.00
gst = price * GST_RATE
 
print(f"{'Product':<15}: {product}")
print(f"{'Price':<15}: Rs {price:,.2f}")
print(f"{'GST (18%)':<15}: Rs {gst:,.2f}")
print(f"{'You pay':<15}: Rs {price + gst:,.2f}")
print("=" * 40)

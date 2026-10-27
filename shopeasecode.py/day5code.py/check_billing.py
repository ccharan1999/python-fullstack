from billing import discount_rate, calculate_bill
assert discount_rate(800) == 0.0
assert discount_rate(1000) == 0.0     # boundary
assert discount_rate(1001) == 0.05
assert discount_rate(6000) == 0.10
bill = calculate_bill({101: 2})       # 2 x Wireless Mouse
assert bill["subtotal"] == 1198.0
assert round(bill["total"], 2) == 1342.96
print("All billing checks passed.")

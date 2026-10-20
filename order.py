def calculate_discount(price, discount_percentage):
    discount = price * discount_percentage / 100
    return discount

print(calculate_discount(1000, 10))

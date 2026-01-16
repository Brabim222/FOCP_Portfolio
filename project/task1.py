#Task 1

print("Beckett Pizza Plaza 4-for-3 Offer")
print("=" * 33)

prices = []
pizza_num = 1

while len(prices) < 4:
    try:
        price = float(input(f"Enter Price of Pizza #{pizza_num}: "))

        if price <= 0:
            print("Please enter a valid price!")
            continue

        prices.append(price)
        pizza_num += 1

    except ValueError:
        print("Please enter a valid price!")

original_total = sum(prices)
cheapest = min(prices)
total = original_total - cheapest
discount = (cheapest / original_total) * 100

print(f"\nOrder Total is £{total:.2f}, a fabulous discount of {discount:.0f}%!")
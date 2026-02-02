def calc_bill(cups, price):
    total_bill = cups * price
    return total_bill

bill = calc_bill(10, 30)

print(f"Bill is {bill}")
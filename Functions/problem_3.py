def add_vat(price, var_rate):
    return price * (100 + var_rate)/100

orders = [100,150,200]

for order in orders:
    final_amount = add_vat(order,10)
    print(f"After VAT, bill is {final_amount}")

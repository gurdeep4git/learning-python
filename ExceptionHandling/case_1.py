class IngredintNotFound(Exception): pass

def process_invoice(flavor, quantity):
    menu = {"masala": 50, "ginger": 70}
    try:
        if flavor not in menu:
            raise IngredintNotFound("This flavor is not on menu.")
        
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        
        total = menu[flavor] * quantity

        print(f"Total bill is {total}")

    except Exception as e:
        print(e)

    finally:
        print(f"Thank You!")


# process_invoice("mint", 50)        
# process_invoice("ginger", "one")        
process_invoice("ginger", 2)        
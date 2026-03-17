class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

p1 = Product("TV", 5000)
p2 = Product("Laptop", 50000)
p3 = Product("Mobile", 2000)

class Cart():
    def __init__(self):
        self.products  = list()

    def add_product(self,product):
        self.products.append(product)
        print(f"{product.name} added in cart")

    def remove_product(self,product):
        for p in self.products:
            if p.name == product.name:
                self.products.remove(product)    
                print(product.name, "removed from cart")
                return
        print("Product not found") 

    def show_cart(self):
        print("Available Products:")
        for p in self.products:
            print(p.name)    

    def cart_total(self):
        total = 0
        for p in self.products:
            total = total + p.price
        return total

    def get_cart_total(self):
        print(f"Cart total is : {self.cart_total()}")


c = Cart()
c.add_product(p1)           
c.add_product(p2)           
c.add_product(p3) 
c.show_cart()
#c.remove_product(p3)
c.show_cart()
c.get_cart_total()


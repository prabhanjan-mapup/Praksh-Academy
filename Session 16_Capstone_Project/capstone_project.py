class Product:
    def __init__(self, product_id, name, price, stock, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def get_product_info(self):
        print(f"Product Id : {self.product_id}")
        print(f"Name : {self.name}")
        print(f"Price : {self.price}")
        print(f"Stock : {self.stock}")
        print(f"Category : {self.category}")

    def add_stock(self, quantity):
        self.stock += quantity

    def remove_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
            
        return False


class RegularProduct(Product):

    def get_product_info(self):
        print(f"Product Id : {self.product_id}")
        print(f"Name : {self.name}")
        print(f"Price : {self.price}")
        print(f"Stock : {self.stock}")
        print(f"Category : {self.category}")
        print(f"Product Type : Regular")

class PerishableProduct(Product):
    def __init__(self, product_id, name, price, stock, category, expiry_date):
        super().__init__(product_id, name, price, stock, category)
        self.expirty_date = expiry_date

    def get_product_info(self):
        print(f"Product Id : {self.product_id}")
        print(f"Name : {self.name}")
        print(f"Price : {self.price}")
        print(f"Stock : {self.stock}")
        print(f"Category : {self.category}")
        print(f"Product Type : Perishable")
        print(f"Expirty Date : {self.expirty_date}")


class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.orders=[]

    def add_order(self, order):
        self.orders.append(order)

    def display_customer(self):
        print(f"Cutomer ID : {self.customer_id}")
        print(f"Name : {self.name}")
        print(f"Phone : {self.phone}")

    def display_order(self):
        print("\n========================")
        print(f"Order History")
        print("==========================")
        if len(self.orders)==0:
            print("No orders found.")
            return 

        for order in self.orders:
            print(
                f"Order ID : {orders.order_id} |"
                f"Amount : ₹{orders.final_amount:.2f} |"
                f"Status : {orders.status}"
            )


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items=[]
        self.subtotal = 0
        self.discount_percentage = 0
        self.discount_amount = 0
        self.final_amount = 0
        self.status = "Pending"

    def add_item(self, product, quantity):
        item={
            "product_id" : product.product_id,
            "name" : product.name,
            "quantity": quantity,
            "price": product.price
        }
        self.items.append(item)
        item_total = product.price * quantity
        self.subtotal += item_total

    def calculate_total(self):
        if self.subtotal >= 10000:
            self.discount_percentage = 15
        elif self.subtotal>=5000:
            self.discount_precentage = 10
        elif self.subtotal >= 1000:
            self.discount_percentage = 5
        else: 
            self.discount_percentage = 0

        self.discount_amount = (
            self.subtotal* self.discount_percentage/100
        )
        self.final_amount = (
            self.subtotal - self.discount_amount
        )

    def display_invoice(self):
        print("\n")
        print("="*60)
        print("         STORE INVOICE")
        print("="*60)
        print(f"Order ID : {self.order_id}")
        print(f"Customer : {self.customer.name}")
        print("-"*60)
        print(
            f"{'Product':<20}"
            f"{'Qty':<8}"
            f"{'Price':<12}"
            f"{'Total':<12}"
        )
        print("-"*60)

        for item in self.items:
            total = (
                item["price"]*item["quantity"]
            )

            print(
                f"{item['name']:<20}"
                f"{item['quanity']:<8}"
                f"{item['price']:<12.2f}"
                f"{total:<12.2f}"
            )

        print("-"*60)
        print(
            f"Subtotal          : ₹{self.subtotal:.2f}"
        )
        print(
            f"Discount          : {self.discount_percentage}%"
        )
        print(
            f"Discount Amount   : ₹{self.discount_amount:.2f}"
        )
        print(
            f"Final Amount      : ₹{self.final_amount:.2f}"
        )
        print(
            f"Order Status      : {self.status}"
        )
        print("="*60)


class StoreManager:
    def __init__(self):
        self.inventory={}
        self.customers={}
        self.orders=[]
        self.categories=set()
        self.order_counter = 1000

    def add_product(self,product):
        if product.product_id in self.inventory:
            print("Product already exists")
            return
        
        if product.price < 0:
            print("Price cannot be negative. ")
            return

        if product.stock < 0:
            print("Stock cannot be negative. ")
            return 

        self.inventory[product.product_id] = product
        self.categories.add(product.category)
        print("Product added successfully")

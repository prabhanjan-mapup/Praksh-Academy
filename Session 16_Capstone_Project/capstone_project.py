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
                f"{item['quantity']:<8}"
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

    def display_inventory(self):
        print("\n")
        print("="*60)
        print("         STORE INVENTORY")
        print("="*60)

        if len(self.inventory) == 0:
            print("Inventory is empty")
            return

        for product in self.inventory.values():
            product.get_product_info()
            print("-"*60)

    def update_stock(self,product_id):
        if product_id not in self.inventory:
            print("Product not found")
            return

        product = self.inventory[product_id]
        print("\n 1. Add stock")
        print("2. Replace stock")

        choice = int(input("Enter choice = "))

        quantity = int(input("Enter quantity = "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        if choice == "1":
            product.add_stock(quantity)
            print("Stock added successfully")
        elif choice == "2":
            product.stock = quantity
            print("Stock replaced successfully")
        else: 
            print("Invalid choice")

    def remove_product(self, product_id):
        if product_id not in self.inventory:
            print("Product not found")
            return

        self.inventory.pop(product_id)
        print("Product removed successfully")

    
    def register_customer(self):
        customer_id = input("Enter customer id : ")
        if customer_id in self.customers:
            print("Customer already exists")
            return
        
        name = input("Enter Customer Name = ")
        phone= input("Enter Phone Number = ")

        customer = Customer(
            customer_id, 
            name,
            phone
        )

        self.customers[customer_id] = customer

    def display_customer(self):
        print("\n")
        print("="*60)
        print("         CUSTOMER")
        print("="*60)

        if len(self.customers) == 0:
            print("No customers found.")
            return

        for customer in self.customers.values():
            customer.display_customer()
            print("-"*60)

    def create_order(self):
        customer_id = input("Enter Customer ID : ")
        if customer_id not in self.customers:
            print("Customer not found")
            return
        
        customer = self.customers[customer_id]
        self.order_counter+=1
        order_id = "O"+str(self.order_counter)
        order = Order(
            order_id, 
            customer
        )
        while True:
            product_id = input("\nEnter Product ID(0 to finish) = ")
            if product_id == "0":
                break
            if product_id not in self.inventory:
                print("Product not found.")
                continue
            product = self.inventory[product_id]
            quantity = int(input("Enter Quantity"))
            if quantity<0:
                print("Quantity cannot be less than zero")
                continue
            if quantity > product.stock:
                print(
                    f"Only {product.stock}"
                    f"units are available"
                )
                continue

            order.add_item(
                product,
                quantity
            )
            product.remove_stock(quantity)
            print("Product added to order. ")

            if len(order.items) == 0:
                print("Order Cancelled\nNo products selected")
                return 

            order.calculate_total()
            order.status="Confirmed"
            self.orders.append(order)
            customer.add_order(order)
            print("\nOrder created successfully")
            order.display_invoice()

    def view_order_history(self):
        customer_id = input("Enter Customer Id = ")
        if customer_id not in self.customers: 
            print("Customer not found")
            return 

        customer = self.customers[customer_id]
        customer.display_order()

    def search_product(self):
        search = input(
            "Enter Product ID, Name or Category"
        ).lower()

        found = False

        for product in self.inventory.values():
            if(
                search == product.product_id.lower()
                or search == product.name.lower()
                or search == product.category.lower()
            ):
                product.get_product_info()
                print("-"*60)
                found = True

        if not found:
            print("Product not found")

    def store_summary(self):
        total_units = 0
        total_sales = 0
        
        highest_price = 0
        highest_product = ""

        lowest_price = 0
        lowest_product = ""

        first_product = True

        for product in self.inventory.values():
            total_units += product.stock

            if first_product: 
                highest_price = product.price
                highest_product = product.name

                lowest_price = product.price
                lowest_product = product.name

                first_product = False

            else : 
                if product.price > highest_price:
                    highest_price = product.price
                    highest_product = product.name

                if product.price < lowest_price:
                    lowest_price = product.price
                    lowest_product = product.name

        
        for order in self.orders:
            if order.status == "Confirmed":
                total_sales += order.final_amount

        print("\n")
        print("="*60)
        print("         STORE SUMMARY")
        print("="*60)

        print(
            f"Total Products    :"
            f"{len(self.inventory)}"
        )
        print(
            f"Total Units   :"
            f"{total_units}"
        )
        print(
            f"Total Customers   :"
            f"{len(self.customers)}"
        )
        print(
            f"Total Orders  :"
            f"{len(self.orders)}"
        )
        print(
            f"Total Sales   :"
            f"₹{total_sales:.2f}"
        )
        print(
            f"Highest Priced Item   :"
            f"{highest_product}"
        )
        print(
            f"Lowest Priced Item   :"
            f"{lowest_product}"
        )
        print(
            f"Categories    :"
            f"{self.categories}"
        )

        print("="*60)




store = StoreManager()

rice = RegularProduct(
    "P101",
    "Rice",
    60,
    20,
    "Food"
)

milk = PerishableProduct(
    "P102",
    "Milk",
    40,
    20,
    "Food",
    "27-08-2026"
)

laptop = RegularProduct(
    "P103",
    "Laptop",
    120000,
    10,
    "Electronics"
)

notebook = RegularProduct(
    "P104",
    "Notebook",
    70,
    100,
    "Stationery"
)

oil = PerishableProduct(
    "P105",
    "Cooking Oil",
    160,
    100,
    "Food",
    "25-01-2027"
)

store.add_product(rice)
store.add_product(milk)
store.add_product(laptop)
store.add_product(notebook)
store.add_product(oil)


while True:
    print("\n")
    print("=" * 50)
    print("          STORE MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Product")
    print("2. Display Inventory")
    print("3. Update Stock")
    print("4. Remove Product")
    print("5. Register Customer")
    print("6. Display Customers")
    print("7. Create Purchase Order")
    print("8. View Order History")
    print("9. Search Product")
    print("10. Store Summary")
    print("0. Exit")

    print("=" * 50)

    choice = input("Enter your choice : ")

    if choice == "1":
        product_id = input(
            "Product ID: "
        )
        name = input(
            "Product Name: "
        )
        price = float(
            input("Price: ")
        )
        stock = int(
            input("Stock: ")
        )
        category = input(
            "Category: "
        )

        print("\n1. Regular Product")
        print("2. Perishable Product")

        product_type = input("Product Type: ")

        if product_type == "1":
            product = RegularProduct(
                product_id, 
                name,
                price,
                stock,
                category
            )
        elif product_type == "2":
            expiry = input("Expiry Date: ")
            product = PerishableProduct(
                product_id,
                name,
                price,
                stock,
                category,
                expiry
            )
        else : 
            print("Invalid product type.")
            continue

        store.add_product(product)

    elif choice == "2":
        store.display_inventory()
    elif choice == "3":
        product_id = input("Enter Product Id: ")
        store.update_stock(product_id)
    elif choice == "4":
        product_id = input("Enter Product")
        store.remove_product(product_id)
    elif choice == "5":
        store.register_customer()
    elif choice == "6":
        store.display_customer()
    elif choice == "7":
        store.create_order()
    elif choice == "8":
        store.view_order_history()
    elif choice == "9":
        store.search_product()
    elif choice == "10":
        store.store_summary()
    elif choice == "0":
        print("\nThan you for using Store Management System")
        break
    else : 
        print("Invalid choice. Please try again.")
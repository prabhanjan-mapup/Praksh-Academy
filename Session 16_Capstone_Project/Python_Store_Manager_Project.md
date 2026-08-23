# Python Mini Project – Store Management System

## Store Manager: Inventory, Customers & Purchase Orders

### Project Difficulty
Intermediate / Advanced Beginner

## Project Overview
Build a command-line Store Management System combining the Python concepts learned so far. The store should maintain products and inventory, register customers, create purchase orders, calculate discounts, update stock, generate invoices, and display summaries.



## Recommended Class Structure
```text
Product
├── RegularProduct
└── PerishableProduct

Customer
Order
StoreManager
```

## 1. Product Class
Create `Product` with:
- product_id
- name
- price
- stock
- category

Create methods such as `display_product()`, `update_stock()` and `sell()`.

## 2. Product Types and Polymorphism
Create `RegularProduct` and `PerishableProduct` inheriting from `Product`.
Override a common method such as `get_product_info()`.

A regular product might show:
```text
Product Type: Regular
```
A perishable product might additionally show:
```text
Product Type: Perishable
Expiry Date: 30-09-2026
```
The StoreManager should call `product.get_product_info()` without checking the concrete class. This demonstrates polymorphism.

## 3. Customer Class
Create `Customer` with:
- customer_id
- name
- phone
- orders (list)

Provide methods to display details, add an order and display order history.

## 4. Order Class
Create `Order` with:
- order_id
- customer
- purchased products
- total amount
- order status

An order can contain multiple items, for example:
```python
[
    {"product_id": "P101", "name": "Rice", "quantity": 2, "price": 60}
]
```

## 5. StoreManager Class
Maintain:
- `inventory`: dictionary mapping Product ID to Product object
- `customers`: dictionary mapping Customer ID to Customer object
- `orders`: list of Order objects
- `categories`: set of unique categories

## 6. Add Product
Ask for Product ID, name, price, stock, category and product type. Reject duplicate IDs and invalid negative price/stock.

## 7. Display Inventory
Display every product neatly, e.g.:
```text
ID       Name       Price   Stock
P101     Rice       60      25
P102     Laptop     55000   8
```
Use iteration and the polymorphic product information method.

## 8. Update Inventory
Allow the user to add stock or replace stock. Handle missing Product IDs.

## 9. Remove Product
Remove a product by ID. Handle missing IDs.

## 10. Register Customer
Ask for Customer ID, name and phone. IDs must be unique.

## 11. Create Purchase Order
The user selects a customer and then one or more products and quantities. The program must:
1. Validate the customer.
2. Validate the product.
3. Validate quantity and stock.
4. Calculate item totals.
5. Add items to the order.
6. Reduce inventory automatically.
7. Allow multiple products in one order.
8. Calculate the final amount.

## 12. Order Calculation
For each item:
```text
Item Total = Price × Quantity
```
Then calculate the subtotal.

## 13. Discount Rules
| Order Amount | Discount |
|---|---:|
| Below ₹1,000 | 0% |
| ₹1,000–₹4,999 | 5% |
| ₹5,000–₹9,999 | 10% |
| ₹10,000 or more | 15% |

Calculate subtotal, discount percentage, discount amount and final amount.

## 14. Inventory Update
If Rice has stock 20 and a customer buys 5, stock must automatically become 15.

## 15. Invoice
Generate a readable invoice such as:
```text
========================================
              STORE INVOICE
========================================
Order ID    : O1001
Customer    : Rahul
----------------------------------------
Product        Qty      Price      Total
Rice             2        60         120
Milk             3        40         120
Notebook         5        50         250
----------------------------------------
Subtotal                  ₹490
Discount                  ₹0
Final Amount              ₹490
Order Status: Confirmed
========================================
```

## 16. Order History
Allow a customer to view previous orders, including order ID, amount and status.

## 17. Search Product
Search by Product ID, name or category. Where appropriate, make text matching case-insensitive.

## 18. Store Summary
Display:
- Total products
- Total units in stock
- Total customers
- Total orders
- Total sales
- Unique categories
- Optionally highest/lowest priced product and most expensive order

## 19. Main Menu
Use a `while` loop:
```text
====================================
        STORE MANAGEMENT SYSTEM
====================================
1. Add Product
2. Display Inventory
3. Update Stock
4. Remove Product
5. Register Customer
6. Display Customers
7. Create Purchase Order
8. View Order History
9. Search Product
10. Store Summary
0. Exit
Enter your choice:
```

## 20. Functions / Methods
Separate responsibilities rather than putting all logic in the menu. Suggested StoreManager methods:
- `add_product()`
- `display_inventory()`
- `update_stock()`
- `remove_product()`
- `register_customer()`
- `create_order()`
- `search_product()`
- `store_summary()`

## 21. Required Data Structures
Use all four meaningfully:
- List: order items, customer order history, all orders
- Tuple: fixed store information, e.g. `("Pune", "Maharashtra", "India")`
- Set: unique categories
- Dictionary: inventory and customers
- Nested collections: at least one nested list/dictionary structure

## 22. Inheritance Requirement
Use:
```text
Product
├── RegularProduct
└── PerishableProduct
```
Child classes inherit common product data and behavior.

## 23. Polymorphism Requirement
Both child classes must override the same method, e.g. `get_product_info()`. Iterate over Product objects and call that method without checking their concrete type.

## 24. Constructor Requirement
Use `__init__()` for classes and initialize attributes through constructors.

## 25. Validation Rules
Handle:
- duplicate Product ID
- negative price or stock
- duplicate Customer ID
- invalid Product ID
- invalid Customer ID
- quantity <= 0
- quantity greater than stock
- invalid menu choice

## 26. Starting Data
Use at least:
```text
P101 - Rice - ₹60 - Stock 20 - Food
P102 - Milk - ₹40 - Stock 15 - Food
P103 - Laptop - ₹55000 - Stock 5 - Electronics
P104 - Notebook - ₹50 - Stock 30 - Stationery
P105 - Cooking Oil - ₹120 - Stock 10 - Food
```
At least one starting product must be a `PerishableProduct`.

## 27. Sample User Flow
```text
Register Customer
Customer ID: C101
Name: Rahul
Phone: 9876543210

Create Purchase Order
Customer ID: C101
Product ID: P101
Quantity: 3
Product ID: P104
Quantity: 5
Finish Order
```
Expected calculation:
```text
Rice: 60 × 3 = 180
Notebook: 50 × 5 = 250
Subtotal = 430
Discount = 0
Final Amount = 430
```
Inventory becomes:
```text
Rice = 17
Notebook = 25
```

## 28. Optional Advanced Features
- Order cancellation with stock restoration
- Low-stock alert for stock below 5
- Loyalty discount after 5 completed orders
- Payment method: Cash / UPI / Card
- Category report

## 29. Restrictions
- No external libraries
- No database
- No file handling unless separately requested
- No frameworks
- Do not copy a complete solution

## 30. Required Concepts Checklist
- [ ] Variables
- [ ] Input / Output
- [ ] Type casting
- [ ] Arithmetic operators
- [ ] Comparison operators
- [ ] Logical operators
- [ ] if-elif-else
- [ ] for loop
- [ ] while loop
- [ ] Nested loops
- [ ] List
- [ ] Tuple
- [ ] Set
- [ ] Dictionary
- [ ] Nested collections
- [ ] Collection methods
- [ ] Functions
- [ ] Parameters
- [ ] Return values
- [ ] Classes
- [ ] Objects
- [ ] `__init__()`
- [ ] Instance attributes
- [ ] Instance methods
- [ ] Inheritance
- [ ] Method overriding
- [ ] Polymorphism

## 31. Final Goal
Build a working command-line store application. Build it incrementally:
1. Create classes.
2. Add initial products.
3. Display inventory.
4. Register customers.
5. Create orders.
6. Update inventory.
7. Generate invoices.
8. Add the menu.
9. Add validation.
10. Demonstrate inheritance and polymorphism.
11. Test every feature.

Before submitting, be able to explain why each class and data structure was chosen and where inheritance and polymorphism occur.

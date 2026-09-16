sales = (
    ('Ali', 'Laptop', 1200),
    ('Sara', 'Phone', 800),
    ('Ali', 'Phone', 800),
    ('Reza', 'Laptop', 1200),
    ('Sara', 'Laptop', 1200),
    ('Ali', 'Mouse', 50)
)
customer_sales = {}
product_sales = {}
total_sales = 0
for sale in sales:
    customer = sale[0]
    product = sale[1]
    price = sale[2]
    if customer in customer_sales:
        customer_sales[customer] = customer_sales[customer] + price
    else:
        customer_sales[customer] = price
    if product in product_sales:
        product_sales[product] = product_sales[product] + 1
    else:
        product_sales[product] = 1
    total_sales = total_sales + price
print('Customer sales:')
for customer in customer_sales:
    print(customer, '->', customer_sales[customer])
best_customer = ''
highest_purchase = 0
for customer in customer_sales:
    amount = customer_sales[customer]
    if amount > highest_purchase:
        highest_purchase = amount
        best_customer = customer
print('Customer with highest purchase:')
print(best_customer)
print(highest_purchase)
print('Product sales:')
for product in product_sales:
    print(product, '->', product_sales[product])
print('Total sales:', total_sales)
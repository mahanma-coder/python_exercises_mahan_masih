products = {
    'P01': ('Laptop', 1200, 5),
    'P02': ('Phone', 800, 0),
    'P03': ('Tablet', 500, 12),
    'P04': ('Mouse', 50, 25),
    'P05': ('Keyboard', 100, 0)}
inventory_values = {}
total_warehouse_value = 0
print('Available products:')
for code in products:
    data = products[code]
    name = data[0]
    price = data[1]
    stock = data[2]
    if stock > 0:
        print(code, name, stock)
    value = price * stock
    inventory_values[code] = value
    total_warehouse_value = total_warehouse_value + value
print()
print('Out of stock:')
for code in products:
    data = products[code]
    name = data[0]
    stock = data[2]
    if stock == 0:
        print(code, name)
print()
print('Inventory values:')
for code in inventory_values:
    print(code, inventory_values[code])
most_valuable_code = ''
highest_value = 0
for code in inventory_values:
    value = inventory_values[code]
    if value > highest_value:
        highest_value = value
        most_valuable_code = code
print()
print('Most valuable product:')
print(products[most_valuable_code][0])
print('Value:', highest_value)
print('Total warehouse value:', total_warehouse_value)
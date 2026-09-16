products = {'laptop': 1200,'phone': 800,'tablet': 500,'headphone': 150,'mouse': 50}
highest_price = products['laptop']
lowest_price = products['laptop']
most_expensive = 'laptop'
cheapest = 'laptop'
total = 0
for name in products:
    price = products[name]
    if price > highest_price:
        highest_price = price
        most_expensive = name
    if price < lowest_price:
        lowest_price = price
        cheapest = name
    total = total + price
average = total / len(products)
print('Most expensive:', most_expensive)
print("Price:", highest_price)
print('Cheapest:', cheapest)
print('Price:', lowest_price)
print('Average:', average)
print('Products over 500:')
for name in products:
    price = products[name]
    if price > 500:
        print(name, price)
print(' Total:', total)
     
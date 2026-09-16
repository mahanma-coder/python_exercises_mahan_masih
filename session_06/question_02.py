inventory = {'apple': 20,'banana': 5,'orange': 0,'milk': 12,'bread': 0}
available = []
out_of_stock = []
for i in inventory:
    stock = inventory[i]
    if stock > 0:
        available.append(i)
    else:
        out_of_stock.append(i)
print('Number of available products:', len(available))
print('Number of out of stock products:', len(out_of_stock))
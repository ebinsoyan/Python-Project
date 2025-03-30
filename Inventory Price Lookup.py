def get_product_price(product_name, inventory):
  return inventory.get(product_name, "Product not found")

#Sample inventory dictionary
inventory = {
"Apple": 1.2,
"Banana": 0.5,
"Orange": 0.8,
"Milk": 2.5,
"Bread": 1.5
}

#User input to look up a product
product_name = input("Enter product name: ")
pn=product_name.capitalize()
price = get_product_price(pn, inventory)
print(f"Price: {price}")

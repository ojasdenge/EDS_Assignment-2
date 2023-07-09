import csv
# Read the data from Sales.csv
product_list = []
supplier_dict = {}
customer_list = []
female_customers = 0
with open('/content/drive/MyDrive/Colab Notebooks/Files/Practical2.csv', 'r') as file:
reader = csv.reader(file)
next(reader) # Skip the header row

# Store Product details in a List data structure
for row in reader:
product_list.append(row[0])

# Store Supplier details in a Dictionary data structure
supplier = row[1]
product = row[0]
if supplier in supplier_dict:
supplier_dict[supplier].append(product)
else:
supplier_dict[supplier] = [product]

# Store Customer details in a Tuple data structure
customer = row[2]
gender = row[3]
customer_list.append((customer, gender))

# Find the number of customers who are 'Female'
if gender == 'Female':
female_customers += 1

# Find the most popular product for sale
most_popular_product = max(set(product_list), key=product_list.count)

# Find the best supplier for sales
best_supplier = max(supplier_dict, key=lambda k: len(supplier_dict[k]))

# Find the customer who buys the most products
customer_most_products = max(customer_list, key=lambda x: product_list.count(x[0]))

# Output the results
print("Most popular product:", most_popular_product)
print("Best supplier:", best_supplier)
print("Customer who buys the most products:", customer_most_products[0])
print("Number of customers who are 'Female':", female_customers)
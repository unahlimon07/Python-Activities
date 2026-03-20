

# List within list

# the List contains the following data about a grocery stores' sales by the month of November(30 days)
# Each item is represented as a list containing:
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
november_sales = [
    ['Chicken', 150, 'Food', 'Standard VAT', 804, 1200],
    ['Hotdog', 50, 'Food', 'Standard VAT', 1200, 2000],
    ['Rice', 40, 'Food', 'Zero-Rated', 1500, 2500],
    ['Bread', 30, 'Food', 'Standard VAT', 900, 1500],
    ['Soap', 25, 'Non-Food', 'Standard VAT', 600, 1000],
    ['Shampoo', 120, 'Non-Food', 'Standard VAT', 450, 800],
    ['Vitamins', 300, 'Health', 'VAT-Exempt', 300, 600],
    ['Medicine', 500, 'Health', 'VAT-Exempt', 200, 400],
    ['Notebook', 80, 'Stationery', 'Standard VAT', 750, 1200],
    ['Pen', 15, 'Stationery', 'Standard VAT', 1000, 1500],
    ['Pencil', 10, 'Stationery', 'Standard VAT', 1100, 1600],
    ['Eraser', 5, 'Stationery', 'Standard VAT', 950, 1400],
    ['Juice', 60, 'Food', 'Standard VAT', 850, 1300],
    ['Soda', 40, 'Food', 'Standard VAT', 950, 1400],
    ['Vegetables', 70, 'Food', 'Zero-Rated', 1300, 2000],
    ['Fruits', 90, 'Food', 'Zero-Rated', 1250, 1900],
    ['Toothpaste', 80, 'Non-Food', 'Standard VAT', 500, 900],
    ['Toothbrush', 60, 'Non-Food', 'Standard VAT', 550, 950],
    ['Bandages', 150, 'Health', 'VAT-Exempt', 400, 700],
    ['Calculator', 200, 'Stationery', 'Standard VAT', 300, 500],
] 
# with the given data on november sales, get the following information:

# easy:
# - [1] total number of items sold
# - [2] total number of sold items per category
# - [3] total sales amount
# - [4] total sales amount per category
# - [5] average price of items per category


print('-----------------[ [1] total number of items sold]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here

total_items_sold = 0

for item in november_sales:
    total_items_sold = total_items_sold + item[4]

print (f'Total number ot items sold: {total_items_sold}\n')

# expected output
# Total number of items sold: 15854


print('-----------------[ [2] total number of sold items per category]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here
# we are finding quantity here

food = 0
non_food = 0
health = 0
stationery = 0


for item in november_sales:
    if item[2] == "Food":
        food += item[4]
    elif item [2] == "Non-Food":
        non_food += item[4]
    elif item [2] == "Health":
        health += item[4]
    elif item [2] == "Stationery":
        stationery += item[4]

print (f'Food sold: {food}')
print (f'Non-Food sol: {non_food}')
print (f'Health: {health}')
print (f'Stationery: {stationery}\n')

# expected output
# food sold: 8754
# non-food sold: 2100
# health sold: 900
# stationery sold: 4100
# total sold: 15854


print('-----------------[ [3] total sales amount]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here

total_sales = 0

for item in november_sales:
    total_sales += item[1]*item[4]

print(f'Total Sales: {total_sales}\n')
    

# expected output
# total sales: 1102850

print('-----------------[ [4] total sales amount per category]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here

food_sales = 0
non_food_sales = 0
health_sales = 0
stationery_sales = 0

for item in november_sales:
    if item [2] == "Food":
        food_sales += item[1]*item[4]
    elif item [2] == "Non-Food":
        non_food_sales += item[1]*item[4]
    elif item [2] == "Health":
        health_sales += item[1]*item[4]
    elif item [2] == "Stationery":
        stationery_sales += item[4]

print(f'Food Sales: {food_sales}')
print(f'Non-Food Sales: {non_food_sales}')
print(f'Health Sales: {health_sales}')
print(f'Stationery Sales: {stationery_sales}\n')

# expected output
# food sales: 560100
# non-food sales: 142000
# health sales: 250000
# stationery sales: 150750
# total sales: 1102850


print('-----------------[ [5] average price of items per category]------------------')
# [Item Name, Price, Category, VAT Type, sold items quantity, remaining stock quantity]
# Categories: Food, Non-Food, Health, Stationery
# type code here

food_ave = 0
non_food_ave = 0
health_ave = 0
stationery_ave = 0

food_count = 0
non_food_count = 0
health_count = 0
stationery_count = 0

for item in november_sales:
    if item[2] == "Food":
        food_count += 1
    elif item [2] == "Non-Food":
        non_food_count += 1
    elif item [2] == "Health":
        health_count += 1
    elif item [2] == "Stationery":
        stationery_count += 1

for item in november_sales:
    if item [2] == "Food":
        food_ave += item[1]/food_count
    elif item [2] == "Non-Food":
        non_food_ave += item[1]/non_food_count
    elif item [2] == "Health":
        health_ave += item[1]/health_count
    elif item [2] == "Stationery":
        stationery_ave += item[1]/stationery_count

print(f'Food Price Average: {food_ave}')
print(f'Non-Food Average: {non_food_ave}')
print(f'Health Average: {health_ave}')
print(f'Stationery Average: {stationery_ave}\n')

# expected output
# food price average: 66.25
# non-food price average: 71.25
# health price average: 316.6666666666667
# stationery price average: 62.0






#list of dictionary
data = [
    {"item":"Fish","category":"Food","subcategory":"Seafood","price":120,"qt_sold_june":400,"qt_sold_july":425},
    {"item":"Beef","category":"Food","subcategory":"Meat","price":400,"qt_sold_june":250,"qt_sold_july":300},
    {"item":"Egg","category":"Food","subcategory":"Dairy & Eggs","price":10,"qt_sold_june":4125,"qt_sold_july":4500},
    {"item":"Pen","category":"Non-Food","subcategory":"Stationery","price":20,"qt_sold_june":312,"qt_sold_july":401},
]


print('-----------------[1] printing all elements------------------')

for item in data:
    print(item)

print('\n\n')

print('-----------------[2] printing name part------------------')

for item in data:
    print(item['item'])


print('-----------------[3] getting june sales------------------')

for item in data:
    print(item['item'], ': ', item['price']*item['qt_sold_june'])


# create the for-in-range equivalent of the above code
# My activity for lesson 2
print('-----------------[4] for-in-range equivalent------------------')
for category in range (len(data)):
    print(data[category]["item"], ":" , data[category]["price"]*data[category]["qt_sold_june"])
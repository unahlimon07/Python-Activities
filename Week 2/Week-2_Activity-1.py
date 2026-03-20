

# Activity: Lists within a List

# List of staff names and the money they have collected from people,

# now, the manager takes 17%, 
# unit head takes 10%, 
# the staff takes 5%, 
# and the rest goes to the company.


# print the total amount collected (get the sum)
# average amount collected (get the average)
# managers portion
# unit head's portion
# company's portion
# staff's portion

names_payment = [
    ['John', 6700],
    ['Jane', 7200],
    ['Doe', 5600],
    ['Alice', 8100],
    ['Bob', 4500],
    ['Eve', 9000],
    ['Charlie', 6200],
    ['Dave', 7300],
    ['Faythe', 4800],
    ['Grace', 5900]
]

total = 0
average = 0
manager = 0
unit_head = 0
company = 0
staff = 0

for name in names_payment:
    total += name[1]
    average += name[1]/len(names_payment)
    manager += name[1]*0.17
    unit_head += name[1]*0.10
    company += name[1]*0.68

print(f'Total: {total}')
print(f'Average: {average}')
print(f'Manager: {manager}')
print(f'Unit Head: {unit_head}')
print(f'Company: {company}')

for name in names_payment:
    print (name[0], name[1]*0.05)





# Expected output:

# total: 65300
# average: 6530.0
# manager: 11101.0
# unit head: 6530.0
# company: 44404.0
# John 335.0
# Jane 360.0
# Doe 280.0
# Alice 405.0
# Bob 225.0
# Eve 450.0
# Charlie 310.0
# Dave 365.0
# Faythe 240.0
# Grace 295.0
    

    
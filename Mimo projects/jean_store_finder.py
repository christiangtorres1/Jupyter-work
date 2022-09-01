# This app is made to check the inventory and goals of the jeans store.
# To run change the integers and run application.

sales = 500
initial_inventory = 750
target = 450
current_inventory = initial_inventory - sales
hit_target = True

print('August 2022 Sales report:')
print(f'Sales this month were {sales} pairs of jeans.')

print('Target report:')

print(f'Our target was {target}')

if hit_target == True:
    print(f'We hit our goal of {target} jeans by {sales - target}.')
else:
    print(f'We need to sell more jeans! We are short {target - sales}')


if hit_target == True:
    print(f'We beat our target by {sales - target}')
else:
    print(f'We are short {target - sales}')

print('Inventory Report:')
print(f'We now have an inventory of {current_inventory}')
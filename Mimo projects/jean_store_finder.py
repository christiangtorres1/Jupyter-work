# This app is made to check the inventory of the jeans store.

sales = 500
initial_inventory = 750
target = 450
current_inventory = initial_inventory - sales
hit_target = True

print('August 2022 Sales report')
print(f'Sales this month were {sales}')

if hit_target == True:
    print('We did it')
else:
    print("We need to sell more jeans!")

print('Target report:')
print('Our target was 450 jeans sold')
if hit_target == True:
    print(f'We beat our target by {sales - target}')
else:
    print(f'We are short {target - sales}')

print(f'We now have an inventory of {current_inventory}')
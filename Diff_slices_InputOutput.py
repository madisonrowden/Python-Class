# Establish how many slices are in a pizza
slices_per_pizza = 8

# Ask How many slices each family member will eat
person1_slices = int(input("How many slices will family member 1 eat? "))
person2_slices = int(input("How many slices will family member 2 eat? "))
person3_slices = int(input("How many slices will family member 3 eat? "))
person4_slices = int(input("How many slices will family member 4 eat? "))

# Calculate the total slices eaten 
total_slices_eaten = person1_slices + person2_slices + person3_slices + person4_slices

# Calculate how many pizzas are needed 
total_pizzas = (total_slices_eaten + slices_per_pizza -1)//slices_per_pizza

# Calculate how many pizza slices there are in total
total_slices = total_pizzas * slices_per_pizza

# Calculate remaining slices
remaining_slices = total_slices - total_slices_eaten

#Display how manya pizzas are needed and how many slices will be left over
print(f'They will need {total_pizzas} pizzas ', end = ' ')
print(f'and there will be {remaining_slices} slices left.')

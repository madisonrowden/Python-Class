#Establish how many cupcakes and muffins there are to start and figure out what the customer wants
muffins = 10
cupcakes = 10
buying = input("Would you like a muffin or a cupcake? ")

#Calculate how much is left after the customer orders
while buying != "0":
    if buying == "muffin":
        if muffins > 0:
            muffins -= 1
            if muffins == 0:
                print("Muffins are out of stock.")
        else:
            print("Muffins are out of stock.")

    elif buying == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
            if cupcakes == 0:
                print("Cupcakes are out of stock.")
        else:
            print("Cupcakes are out of stock.")
    buying = input("Would you like a muffin or a cupcake? ")

#Display how many muffins and cupcakes are left
print("muffins:", muffins, "cupcakes:", cupcakes)

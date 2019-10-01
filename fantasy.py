def add_to_inventory(inventory, added_item):
    for i in added_item:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.update({i: 1})



def print_table(inventory, order):


    x = 101
    for k in range(0,101):
        for j in inventory:
            if int(inventory[j]) == x:
                inv.update({j :(inventory[j])})
        x -= 1




    print("-----------------\nitem name | count\n-----------------")
    for i in inv:
        print("{} | {}".format(i, (inv[i])))
    print("-----------------")




def export_inventory(inventory, filename):
    with open("export_inventory.csv", "w") as x:
        for i in inventory:
            x.write("{0}: {1} \n".format(i,inventory[i]))


add_to_inventory(bag, dragon_loot)
display_inventory(bag)
print_table(bag, None)
export_inventory(inv, f)

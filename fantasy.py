bag = {'rope': 1, 'torch': 6,
       'gold coin': 42, 'dagger': 1,
       'arrow': 12
       }

dragon_loot = ['gold coin', 'dagger',
               'gold coin', 'gold coin',
               'ruby'
               ]
with open("export_inventory.csv", "a") as f:
    f.write("")

with open("importinventory.csv", "a") as k:
    k.write("")



list_inv= []
inv = {}
def display_inventory(inventory):
    for i in inventory:
        print("{}: ".format(i), end="")
        print(inventory[i])


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

def import_inventory(inventory, filename):
    import csv
    with open("importinventory.csv", "r") as x:
        l = csv.reader(x)
        for i in l:
            for j in i:
                inventory.append(j)
        print(inventory)


def export_inventory(inventory, filename):
    import csv
    with open("export_inventory.csv", "w") as x:
        for i in inventory:
            x.write("{0}: {1} \n".format(i,inventory[i]))


add_to_inventory(bag, dragon_loot)
display_inventory(bag)
print_table(bag, None)
import_inventory(list_inv,k)
export_inventory(inv, f)

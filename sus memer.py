import random

beglst = ["You begged for your life in Spanish and gained","Today is your lucky day, you earned","Here you go, have","You can have","Nah, no thanks :)","I dont care","Try again later","No"]

searchlst = ["bin", "school", "grass", "area51", "home", "laundromat"]

shopdict = {"horseshoe": 50000}
shopdesc = [" Increases luck by 1%"]

balance = 0

inventory = {"nothing": 0, "horseshoe": 0}

commands = ["help","?","beg","search","scout","balance","bal","shop","buy","purchase","inventory","inv"]
print("VERSION 20/2/2023, DO NOT LEAVE INPUTS BLANK, IT WILL CAUSE IT TO CRASH")
pls = input("Try out our commands: pls help ").lower()
while True:
    lst = list(pls.split())
    while pls.isspace() or lst[0] != "pls" or len(lst) < 2:
        if len(lst) < 2 and len(lst) == 1 and lst[0] == "pls":
            pls = input("That is not a valid command, use pls help for available commands ").lower()
        else:
            pls = input("To use our commands, type pls <command> ").lower()
        lst = list(pls.split())
    if lst[0] == "pls":
        if lst[1] == "help" or lst[1] == "?":
            print("Here's a list of all of our commands: pls help, pls beg, pls search, pls balance")
        elif lst[1] == "beg":
            if random.randint(1,2) == 1:
                gain = random.randint(int(0.1*(100+inventory["horseshoe"])),777)
                print(beglst[random.randint(0,3)],gain,"coins")
                balance += gain
            else:
                if inventory["horseshoe"] > 0 and random.randint(1,100) == 69:
                    print("You gained nothing")
                    inventory["nothing"] += 1
                else:
                    print(beglst[random.randint(4,7)])
        elif lst[1] == "search" or lst[1] == "scout":
            searcharea = input("Where would you like to search?{}")
            print("Search command not implemented yet... maybe tmr")
        elif lst[1] == "balance" or lst[1] == "bal":
            print(f"You have {balance} coins")
        elif lst[1] == "shop":
            shopindex = 0
            for item,price in shopdict.items():
                print(f"Item: {item}, Price: {price}, Description: {shopdesc[shopindex]}")
                shopindex += 1
            print("To buy an item, use the command: pls buy <item>")
        elif lst[1] == "buy" or lst[1] == "purchase":
            if len(lst) != 3:
                print("Uhh theres some input error, try again")
            elif lst[2] in shopdict:
                if balance >= shopdict[lst[2]]:
                    inventory[lst[2]] += 1
                    balance -= shopdict[lst[2]]
                    print(f"You bought a {lst[2]} for {shopdict[lst[2]]}, now you have {balance} coins left")
                else:
                    print(f"Insufficient funds, you need {shopdict[lst[2]] - balance} more coins")
            else:
                print("Item not found in the shop")
        elif lst[1] == "inventory" or lst[1] == "inv":
            if tuple(inventory.values()).count(0) == len(inventory):
                print("You have nothing")
            else:
                for items,amount in inventory.items():
                    if amount != 0:
                        print(f"{items.capitalize()}: {amount}")
        else:
            print("Command not found, to see all usuable commands, type: pls help")
        pls = input().lower()
        lst = list(pls.split())
    else:
        pls = input("Try out our commands: pls help ")

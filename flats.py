from tkinter.messagebox import YES
from typing import ValuesView


def is_positive_answer(users_answer):
    positive_answers = [True, "True","true", 1, "1", "yes", "yeah"]
    if users_answer in positive_answers:
        return True  # return má výsledek buď True nebo False
    else:
        return False


def valid_price_rate(min_price, max_price):
    interval = range(int(min_price), int(max_price))
    x = set(interval) | set(range(0, 10_000))
    if 10_001 in x:
        return True


starter = input("Would you like to buy a flat? ")
if not is_positive_answer(starter):
    print("Good bye 🙂")
    exit()

min_price = input("Enter min price: ")  # všechny inputy jsou stringy ""
max_price = input("Enter max price: ")


if not valid_price_rate(min_price, max_price):
    print("There is no such flat. ")
    exit()

print("This is our offer:")
i = 1
while i <= 10:
    if i == 1 or i == 7 or i == 3 or i == 4 or i == 5:
        print(str(i) + ". flat - centre")
    else:
        print(str(i) + ". flat - outskirts")
    i += 1

centr = ["flat one", "flat three", "flat four", "flat five", "flat seven"]

outs = ["flat two", "flat six", "flat eight", "flat nine", "flat ten"]

area = input("Would you like to live in centre or on the outskirts? ")
print("You may choose from this flats:")
if area == "centre":
    for flats in centr:
        print(flats)

else:
    for flats in outs:
        print(flats)

flat_dict = {
    "flat one": {"balcony": "True", "garage": "True", "type": "1+1", "view": "True"},
    "flat two": {"balcony": "False", "garage": "True", "type": "2+1", "view": "False"},
    "flat three": {"balcony": "True", "garage": "True", "type": "1+1", "view": "True"},
    "flat four": {"balcony": "True", "garage": "False", "type": "3+1", "view": "True"},
    "flat five": {"balcony": "True", "garage": "True", "type": "2+1", "view": "False"},
    "flat six": {"balcony": "True", "garage": "False", "type": "1+1", "view": "True"},
    "flat seven": {"balcony": "True", "garage": "True", "type": "3+1", "view": "True"},
    "flat eight": {"balcony": "True", "garage": "True", "type": "2+1", "view": "True"},
    "flat nine": {"balcony": "False", "garage": "True", "type": "3+1", "view": "False"},
    "flat ten": {"balcony": "True", "garage": "False", "type": "1+1", "view": "True"},
}

typ = input("Would you like a flat type: 3+1 or 1+1 or 2+1? ")
view = input("Would you like a view of a city? ")
balcony = input("Would you like a balcony? ")
garage = input("Would you like a garage? ")

def return_flat_type(users_searched_type):  # funkce vrací jen datový typ, ne více řádků
    vysledky0 = []
    for byt in flat_dict:
        if flat_dict[byt]["type"] == users_searched_type:
            vysledky0.append(byt)
    return vysledky0


pani_vratila_typ = return_flat_type(typ)
print("Typy bytů:")
for typy_bytu in pani_vratila_typ:
    print(typy_bytu)



def return_flat_balcony(users_searched_balcony):  
    vysledky1 = []
    for byt in flat_dict:
        if flat_dict[byt]["balcony"]==users_searched_balcony:
            vysledky1.append(byt)
    return vysledky1

pani_vratila_balkon = return_flat_balcony(balcony)
print("Byty:")
for balkony_bytu in pani_vratila_balkon:
    print(balkony_bytu)


def return_flat_view(users_searched_view): 
    vysledky2 = []
    for byt in flat_dict:
        if flat_dict[byt]["view"]==users_searched_view:
            vysledky2.append(byt)
    return vysledky2

pani_vratila_vyhled = return_flat_view(view)
print("Byty:")
for vyhled_bytu in pani_vratila_vyhled:
    print(vyhled_bytu)


def return_flat_garage(users_searched_garage):  
    vysledky3 = []
    for byt in flat_dict:
        if flat_dict[byt]["garage"] == users_searched_garage:
            vysledky3.append(byt)
    return vysledky3

pani_vratila_garaz = return_flat_garage(garage)
print("Byty:")
for garaz_bytu in pani_vratila_garaz:
    print(garaz_bytu)

def return_area(users_area):
    if users_area == "centre":
        final_area_centr= centr
        return final_area_centr
    elif users_area == "outskirts":
        final_area_outs= outs
        return final_area_outs
x=return_area(area)


print("Ideální byt pro vás:")
idealni= set(pani_vratila_garaz)& set(pani_vratila_balkon)& set(pani_vratila_typ)& set(pani_vratila_vyhled) & set(x)
for l in idealni:
    if idealni != None:
        print(l)
    else:
        print("There is no flat for you. ")

def is_positive_answer(users_answer):
    positive_answers= [True, "true", 1, "1", "yes", "yeah"]
    if users_answer in positive_answers:
        return True #return má výsledek buď True nebo False
    else:
        return False

def valid_price_rate(min_price, max_price):
    interval= range(int(min_price), int(max_price))
    x=set(interval)|set(range(0,10_000))
    if 10_001 in x: 
        return True

starter= input ("Would you like to buy a flat? ")
if not is_positive_answer(starter):
    print ("Good bye 🙂")
    exit()

min_price=input("Enter min price: ") # všechny inputy jsou stringy ""
max_price=input("Enter max price: ")



if not valid_price_rate(min_price, max_price):
    print ("There is no such flat.")
    exit()

print("This is our offer:")
i=1
while i<=10:
        if i== 1 or i==7 or i==3 or i==4 or i==5:
            print(str(i) + ". flat - centre")
        else:
            print(str(i) + ". flat - outskirts")
        i+=1

centr=[ "flat one", "flat three", "flat four","flat five",  "flat seven"]

outs=["flat two", "flat six", "flat eight", "flat nine", "flat ten"]

area=input ("Would you like to live in centre or on the outskirts?")
print("You may choose from this flats:")
if area== "centre":
    for flats in centr:
        print(flats)
    
else:
    for flats in outs:
        print(flats)

        flat_dict = {"flat one": {"balcony": "True" , "garage":"True", "type": "1+1", "view": "True"}, "flat two":{"balcony": "True" , "garage":"True", "type": "2+1", "view": "True"}, "flat three": {"balcony": "True" , "garage":"True", "type": "1+1", "view": "True"},"flat four": {"balcony": "True" , "garage":"True", "type": "3+1", "view": "True"}, "flat five": {"balcony": "True" , "garage":"True", "type": "2+1", "view": "True"}, "flat six": {"balcony": "True" , "garage":"True", "type": "1+1", "view": "True"},"flat seven": {"balcony": "True" , "garage":"True", "type": "3+1", "view": "True"}, "flat eight": {"balcony": "True" , "garage":"True", "type": "2+1", "view": "True"}, "flat nine": {"balcony": "True" , "garage":"True", "type": "3+1", "view": "True"},"flat ten": {"balcony": "True" , "garage":"True", "type": "1+1", "view": "True"}}

typ=input("Would you like a flat type: 3+1 or 1+1 or 2+1?")


i=1
def return_flat_type(users_searched_type):
     if typ ==users_searched _type:
          while i<=10: 
            if str(flat_dict["flat"+str(i)["type"])==users_searched_type:
              return "flat "+i

return_flat_type ("3+1") 
              
         
exit()

if typ =="3+1":
 if str(flat_dict["flat 1"]["type"])== "3+1":
     print("flat one")
 if str(flat_dict["flat 2"]["type"])== "3+1":
     print("flat two")
 if str(flat_dict["flat 3"]["type"])== "3+1":
     print("flat three")
 if str(flat_dict["flat 4"]["type"])== "3+1":
     print("flat four")
 if str(flat_dict["flat 5"]["type"])== "3+1":
     print("flat five")
 if str(flat_dict["flat 6"]["type"])== "3+1":
     print("flat six")
 if str(flat_dict["flat 7"]["type"])== "3+1":
     print("flat seven")
 if str(flat_dict["flat 8"]["type"])== "3+1":
     print("flat eight")
 if str(flat_dict["flat 9"]["type"])== "3+1":
     print("flat nine")
 if str(flat_dict["flat 10"]["type"])== "3+1":
     print("flat ten")
     
 

elif typ=="2+1":
    if str(flat_dict["flat one"]["type"])== "2+1":
        print("flat one")
    if str(flat_dict["flat two"]["type"])== "2+1":
        print("flat two")
    if str(flat_dict["flat three"]["type"])== "2+1":
        print("flat three")
    if str(flat_dict["flat four"]["type"])== "2+1":
        print("flat four")
    if str(flat_dict["flat five"]["type"])== "2+1":
        print("flat five")
    if str(flat_dict["flat six"]["type"])== "2+1":
        print("flat six")
    if str(flat_dict["flat seven"]["type"])== "2+1":
        print("flat seven")
    if str(flat_dict["flat eight"]["type"])== "2+1":
        print("flat eight")
    if str(flat_dict["flat nine"]["type"])== "2+1":
        print("flat nine")
    if str(flat_dict["flat ten"]["type"])== "2+1":
        print("flat ten")
        
elif typ=="1+1":
    if str(flat_dict["flat one"]["type"])== "1+1":
        print("flat one")
    if str(flat_dict["flat two"]["type"])== "1+1":
        print("flat two")
    if str(flat_dict["flat three"]["type"])== "1+1":
        print("flat three")
    if str(flat_dict["flat four"]["type"])== "1+1":
        print("flat four")
    if str(flat_dict["flat five"]["type"])== "1+1":
        print("flat five")
    if str(flat_dict["flat six"]["type"])== "1+1":
        print("flat six")
    if str(flat_dict["flat seven"]["type"])== "1+1":
        print("flat seven")
    if str(flat_dict["flat eight"]["type"])== "1+1":
        print("flat eight")
    if str(flat_dict["flat nine"]["type"])== "1+1":
        print("flat nine")
    if str(flat_dict["flat ten"]["type"])== "1+1":
        print("flat ten")
    
from oops import *


ponu1 = Cse_nalla_ponu("mol",17,"white",8,"silent","a+",9.99)
ponu2 = Cse_nalla_ponu("thipsa", 18, "medium", 6, "silent","o" ,8.66)
ponu3 = Cse_nalla_ponu("bavani", 18, "medium", 3, "not bad", "B", 6)
ponu4 = Cse_Items("tamil", "18", "white", 6, 6, 4, 6, 200, "worse")
ponu5 = Cse_Items("jo", 18, "medium", 3, 3, 3, 6, 180, "not bad")
ponu6 = Cse_Items("jomi", 17, "white", 7, 7, 9, 3, 50, "worst")


print("the total number of girls is ",Cse_girls.girls)
print("the total number of items is {}".format(Cse_Items.items))
print("the total number of nala ponu is {}".format(Cse_nalla_ponu.nalla_ponu))

ponu1.get_phone_no()
ponu2.pic()
ponu3.greet()

ponu4.details()
ponu5.get_phone_no()
ponu5.nudepic("gowtham")
ponu6.pickup()

def set_love(ponu,love_status):
    ponu.love = love_status

set_love(Cse_Items, "yes")
set_love(Cse_nalla_ponu, "no")

print(Cse_Items.love)
print(Cse_nalla_ponu.love)


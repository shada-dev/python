import random
from abc import ABC,abstractmethod

if(__name__=="__main__"):
    print("it's running in main file")
    class Cse_girls:
        girls = 0    
        def __init__(self,name,age,color,total,character):
            self.name = name
            self.age = age
            self.color = color
            self.total = total
            self.character = character
            Cse_girls.girls += 1
        
        @abstractmethod
        def get_phone_no(self):
            pass

        @abstractmethod
        def pic(self):
            pass

    class Cse_Items(Cse_girls):
        items = 0  
        love = "no"      
        def __init__(self,name,age,color,butt_size,boobs_size,hip,total,price,character):
            super().__init__(name,age,color,total,character)
            self.boobs_size = boobs_size  #isinstance variable
            self.butt_size = butt_size
            self.hip = hip
            self.price = price
            Cse_Items.items += 1

        def pickup(self):
            print("buying...",self.name)
        
        def nudepic(self,name):
            print("nude pic of {} is here {}".format(self.name,name))

        def details(self):
            print("name :",self.name)
            print("Age :",self.age)
            print("color :",self.color)
            print("Boobs size:",self.boobs_size)
            print("Butt size :",self.butt_size)
            print("Hip size :",self.hip)
            print("total mark :",self.total)
            print("Price :",self.price)

        def get_phone_no(self):
            random_number = random.randint(999999999, 10000000000)
            print("{} this is {}'s number".format(random_number,self.name))

        # def pic(self):
        #     print("This is her pic")  

    class Cse_nalla_ponu(Cse_girls):
        nalla_ponu = 0
        love = "yes"
        def __init__(self,name,age,color,total,character,good_grade,cgpa):
            super().__init__(name,age,color,total,character)
            self.good_grade = good_grade
            self.cgpa = cgpa
            Cse_nalla_ponu.nalla_ponu += 1

        def greet(self):
            print("thank you for preserving good qualities")

        def get_phone_no(self):
            random_number = random.randint(999999999, 10000000000)
            print("{} this is {}'s number".format(random_number,self.name))

        def pic(self):
            print("This is her pic")


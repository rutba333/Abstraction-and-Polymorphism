#class 1
class India():
    def capital(self):
        print("New delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language in India")
        
    def type():
        print("India is a developing country ")


#class 2
class USA():
    def capital(self):
        print("Washington, D.C is the capital of USA")

    def language(self):
        print("English is the primary language of USA")
        
    def type():
        print("USA is a developed country ")

#object creation
obj_Ind=India()
obj_usa=USA()

#common interface
for country in(obj_Ind,obj_usa):
    country.capital()
    country.language()
    country.type()
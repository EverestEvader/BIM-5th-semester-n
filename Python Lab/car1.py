class car:
    country="Nepal"
    def setdetails(self,b,m):
        self.brand=b
        self.model=m
    def changecountry(self,c):
        self.country=c
    @classmethod
    def chgcoun(cls,cntry):
        cls.country=cntry
    def show(self):
        print("Country: ", self.country)
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        

c1=car()
c1.setdetails("BMW","Coupe")
c1.show()
print()
c2=car()
c2.setdetails("Nissan","Sport")
c2.changecountry("Germany")
c2.show()
print()
car.chgcoun("USA")
c1.show()
print()
c2.show()


        

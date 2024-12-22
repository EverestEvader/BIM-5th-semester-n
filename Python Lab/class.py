class student:
    clgname='BMC'
    def sdetails(self,name):
        self.name=name

    def display(self):
        print("Name: ",self.name)
        print("College Name: ",self.clgname)

    @classmethod
    def clame(cls, nname):
        cls.clgname=nname
s1=student()
s1.sdetails("Pragya")
s1.display()
s1.clame("NCC")
s1.display()
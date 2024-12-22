class animal():
    def sound(self):
        print("I sound like an animal")
class dog(animal):
    def sound(self):
        print("I sound like a dog")
class cat(animal):
    def sound(self):
        print("I sound like a cat")
class tiger(animal):
    def sound(self):
        super().sound()
        print("I sound like a tiger")
anim=animal()
d = dog()
c = cat()
t = tiger()
anim.sound()
d.sound()
c.sound()
t.sound()

##2 44
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print("Gav")

ronnie = Animal("RONNIE" , "гав")
ronnie.make_sound()
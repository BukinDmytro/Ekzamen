#10
class Studen:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_info(self):
        print(self.name, self.age)
s=Studen("Andriy",16)
s.get_info()


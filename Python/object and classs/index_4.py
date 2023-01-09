class Car :
    name=""
    color =  ""
    def __init__(self, name, color) :
           self.name=name
           self.color=color
    def start(self) :
         print("Enginre blue power star ")



my_car=Car("bule", "white")
print(my_car.name)
print(my_car.color)
my_car.start()
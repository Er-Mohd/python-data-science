class Animal:

    def __init__(self, name, age, color,region):
        self.name = name
        self.age = age
        self.color = color
        self.region = region
        self.is_domestic = False 

    def info(self):
        print('Animal details')
        print('name:', self.name)
        print('age:', self.age) 
        print('color:', self.color) 
        print('region:', self.region)                                         


o1 = Animal('fish', '5', 'blue', 'africa')
o2 = Animal('Lion', '10', 'yellow', 'india')       


o1.info()
o2.info()
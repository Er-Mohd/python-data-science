class cat:
    name = ""
    age = 0
    fur_color = ""
    breed = ""

    def eat(self):
        print("cat is eating!")

    def sleep(self):
        print("cat is sleeping!")


# creating objects
tom = cat()
snow = cat()
tom.age = "Tom"
tom.fur_color = 'gray'
tom.breed = 'city cat'
snow.name = 'snowbell' 
snow.age = '5'
snow.fur_color = 'white'
snow.breed = 'persian'

#calling method
tom.eat()
snow.sleep()
tom.sleep()

# displaying attributes
print(tom.name, tom.age, tom.fur_color, tom.breed)
print(snow.name, snow.age, snow.fur_color)
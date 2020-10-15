class Person():
    def __init__(self, name, age, gender):  # 在创建实例时进行赋值
        self.name = name
        self.age = age
        self.gender = gender

    def set_att(self, value):
        self.value = value

    def eat(self):
        print(f" name : {self.name},age : {self.age}, gender : {self.gender}, 我在吃")


xiaoming = Person("xiaoming", 10, "male")
xiaoming.eat()
xiaoming.set_att("fat")
print(xiaoming.value)

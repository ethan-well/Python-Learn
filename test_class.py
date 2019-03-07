class Dog():
    def __init__(self, name, age):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is sitting.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rolled over!")

dog = Dog('旺财', 12)
dog.sit()
dog.roll_over()
print(dog.name)
print(dog.age)
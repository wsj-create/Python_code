#类名要用大驼峰定义法
class Cat :
    def eat(self):
        print("小猫要吃鱼")
    def drink(self):
        print("小猫要喝水")


#创建猫对象
tom = Cat()
#调用类里面的方法
tom.eat()
tom.drink()
print(tom)
addr = id(tom)
print(addr)
#TODO 问老师这个十进制地址怎么老是变化



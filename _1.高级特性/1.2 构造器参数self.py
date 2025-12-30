# 1.python构造器与self
class student1():
    def __init__(self,name,age):
        # __修饰的变量相当于被private修饰
        self.__age=age
        # _修饰的变量可以被直接访问,但是最好不要直接访问
        self._name=name
    def getAge(self):
        return self.__age
    # 无论是什么类方法还是构造器,第一参数都应该是self,它指向底层封装的student示例对象自身,结构有点像下列
    # class student_yuan():
    #   self
    #   constructor():
    #       self=student_yuan()

# 2.self代表实例对象
# 如注释代码所示,self指向的是一个示例对象
class instance1():
    def print(self):
        print(self)
        print(self.__class__)
class instance2():
    def print(self):
        print(self)
        print(self.__class__)
t1=instance1()
t2=instance2()
# t1.print(t2)
# TypeError: instance1.print() takes 1 positional argument but 2 were given

# 3.self可以不写吗?
class teacher():
    def __init__(self,name):
        self.name=name

    def getName():
        # print(self.name) 警告
        # 不传入示例对象作为参数,方法内也无法调用成员属性,这样的方法叫做类方法
        print("只能输出一些没有成员参数参与的信息")

# 4.在描述符类中,self指的是描述符类的实例
class Desc:
    # 每次调用实例对象时都会调用__get__方法
    def __get__(self, ins, cls):
        print('self in Desc: %s ' % self )
        print(self, ins, cls)
class Test:
    x = Desc()
    def prt(self):
        print('self in Test: %s' % self)
t = Test()
t.prt()
t.x

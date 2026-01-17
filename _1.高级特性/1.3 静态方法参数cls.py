'''
    1.定义:@classmethod修饰,cls必须为第一个参数的方法
        用途:直接访问类属性(是不是很像静态)
'''
class Example:
    class_var = "类属性"
    def instance_method(self):
        return self.class_var  # 访问类属性 via 实例
    @classmethod
    def class_method(cls):
        return cls.class_var  # 直接访问类属性
obj = Example()
obj.instance_method()  # 实例调用
Example.class_method()  # 类调用

'''
    2.python中的静态(使用@staticmethod修饰)
'''
class MyClass:
    @staticmethod
    def my_static_method():
        print("这是一个静态方法")

# 直接通过类名调用静态方法
MyClass.my_static_method()
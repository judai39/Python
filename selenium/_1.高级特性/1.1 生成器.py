# 使用列表生成式直接生成列表
list=[x * x for x in range(10) if x>0]
# 缺点:列表容量有限,需要遍历所有元素才能取值----使用生成器(通过某种算法直接推出需要的列表元素)

# 使用生成器生成列表(不同于将式子中所有元素遍历得到后全部赋值,生成器允许将式子的逻辑函数赋值,一遍一遍进行赋值)
generator=(x * x for x in range(10) if x>0)
#遍历可以用next()...或for循环

# 可以把生成器的式子逻辑看作函数,那么如何将普通函数变为生成器?  --添加yield关键字
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
# 那么yield添加在哪的依据是?
    # 解释一下生成器的执行顺序:generator函数和普通函数的执行流程不一样。普通函数是顺序执行，遇到return语句或者最后一
    # 行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的
    # yield语句处继续执行。
# 所以yield添加的地方在判断进入下一循环之后,执行当前循环变量逻辑之前

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o=odd()
next(o)
next(o)
next(o)
# next(odd()) x3只会输出三个step1,因为每次调用odd()会实例化三个不同的对象
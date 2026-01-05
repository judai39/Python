import pytest
# 测试方法的执行顺序:
# 1)对于不同的命令行的执行文件:添加顺序决定了不同测试文件的读取顺序
# 2)对于同一执行文件的测试方法:撰写代码的先后决定了读取顺序
# ---->但是代码的撰写者不会根据测试者的需求去严格要求自己的代码严谨性---->如何对已完成的测试文件手动设置测试顺序?
# ---->pytest-order插件
# pip install pytest-ordering
# 注意:run标签是全局生效,运行根目录读取order前后级


# 1.run(参数order,值越小顺序权重越高)
@pytest.mark.run(order=2)
def test_001():
    print("测试方法001")
    assert True

@pytest.mark.run(order=1)
def test_002():
    print("测试方法002")
    assert True

@pytest.mark.run(order=3)
def test_003():
    print("测试方法003")
    assert True
# （；´д｀）ゞ:暂时有问题
# 2.run(参数before,after,相对于当前函数的先后)

# @pytest.mark.run('after')
# def test_mark_run_001():
#     print("类中测试方法_001")
#     assert True
# @pytest.mark.run('first')
# def test_mark_run_002():
#     print("类中测试方法_002")
#     assert True
        
# @pytest.mark.run('last')
# def test_mark_run_003():
#     print("类中测试方法_003")
#     assert True

if __name__=="__main__":
    pytest.main(['-vs','pytest/4_mark/mark_run/mark_run_sample.py'])
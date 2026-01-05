import pytest
# pytest框架如何调试代码
# pip install pytest-pdb安装调试插件
# pytest --pdb test.py
# 也可以在pytest.ini文件中配置addopts选项,添加参数--pdb

def test_error_method():
    index=0
    assert index==1

if __name__=="__main__":
    pytest.main()
from custom_log_sample import Logs
import pytest
import logging

def  test_custom_log_to_console():
    Logs.get_logger().warning("我是自定义日志,我输出了一些内容")


if __name__=="__main__":
    pytest.main(["-s","pytest/6_log/01_log_standard/log_main.py"])
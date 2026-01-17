import logging
import logging.handlers
import os
import time

'''
实现日志记录器功能,首先需要创建日志记录器(logging.getLogger()),控制台输出器(logging.StreamHandler()),
文件流输出器(logging.handlers.TimedRotatingFileHandler),使用格式器初始化两个输出器,再将输出其add到日志记录器上以
完成日志变量logging的组装
注意:使用的单例工厂实现的logging
'''

class Logs:
    # 新建一个日志器变量
    my_logger=None

    # 日志级别关系映射(级别由小到大)
    level_relations={
        # （；´д｀）ゞ:区别大小写(匿名类...)
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'critical':logging.CRITICAL
    }

    # 工厂方法初始化日志器并获取
    @classmethod
    def get_logger(cls,level_stdout='info',level_file='error'):
        if cls.my_logger is None:
            # 获取日志记录器
            cls.my_logger=logging.getLogger('my_logger')
            # 修改默认级别为level_stdout
            cls.my_logger.setLevel(cls.level_relations.get(level_stdout))
            log_path="C:"+os.sep+"Users"+os.sep+"judai"+os.sep+"Desktop"+os.sep+"python"+os.sep+"pytest"+os.sep+"6_log"+os.sep+"01_log_standard"+os.sep+"logs"+os.sep+"{}.log".format(time.strftime("%Y%m%d"))
            # 获取文件输出处理器(用于向文件输出输出日志信息)
            TimedRotatingFileHandler_handlers=logging.handlers.TimedRotatingFileHandler(
                filename=log_path,
                when="midnight",
                interval=1,
                backupCount=3,
                encoding="utf-8"
            )

            # 获取控制台输出处理器(用于向控制台输出信息)
            StreamHandler_handlers=logging.StreamHandler()
            # 获取格式器
            formatter=logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
            # 修改处理器的默认级别为level_file
            TimedRotatingFileHandler_handlers.setLevel(cls.level_relations.get(level_file))
# 等价于cls.my_logger.setLevel(cls.level_relations.get(level_stdout))  会被覆盖
            StreamHandler_handlers.setLevel(cls.level_relations.get(level_stdout))
            # 格式器初始化处理器参数
            TimedRotatingFileHandler_handlers.setFormatter(formatter)
            StreamHandler_handlers.setFormatter(formatter)
            # 处理器添加到日志器
            cls.my_logger.addHandler(TimedRotatingFileHandler_handlers)
            cls.my_logger.addHandler(StreamHandler_handlers)
        return cls.my_logger
'''
get_logger中的参数level_stdout,level_file是指?
    （；´д｀）ゞ:前者值的是命令行输出日志处理器的默认级别,后者是文件输出日志处理器的默认级别
    当使用get_logger().warning()时,如果warning的级别低于日志提醒的最低默认级别,那么对应的输出将不会输出任何信息
'''
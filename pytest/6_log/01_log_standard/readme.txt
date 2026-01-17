在使用log日志之前无可避免的是需要配置log默认配置,以下有三种使用方式的配置方法
1.命令行调用日志
--log-level=LEVEL：设置默认日志等级
--log-format=LOG_FORMAT：设置默认日志格式
--log-date-format=LOG_DATE_FORMAT：设置默认日志日期格式
--log-cli-level=LOG_CLI_LEVEL：设置默认命令行日志等级
--log-cli-format=LOG_CLI_FORMAT：设置默认命令行日志格式
--log-cli-date-format=LOG_CLI_DATE_FORMAT：设置默认命令行日志日期格式
--log-file=LOG_FILE：设置默认日志文件路径
--log-file-level=LOG_FILE_LEVEL：设置默认日志文件等级
--log-file-format=LOG_FILE_FORMAT：设置默认日志文件日志格式
--log-file-date-format=LOG_FILE_DATE_FORMAT：设置默认日志文件日期格式
--log-auto-indent=LOG_AUTO_INDENT：设置多行文本日志缩进，支持true|on, false|off 或整数值。
--log-disable=LOGGER_DISABLE：根据名称禁用某个logger，支持指定多次。

2.pytest.ini配置文件中添加参数
log_print	用例失败时是否显示相关日志；
log_cli	配置为ture时开启命令行日志；
log_file	配置日志文件路径，每次覆盖，不支持追加模式；v
log_cli_level/log_file_level	配置输出到命令行及文件的日志等级；
log_cli_format/log_file_format	配置输出到命令行及文件的日志格式；
log_cli_date_format/log_file_date_format	配置日志的日期格式。

3.log类通过包装器包装
# 配置日志记录，同时输出到控制台和文件
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler('app.log'),
                            logging.StreamHandler()
                        ])
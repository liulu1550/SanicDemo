
class BaseConfig(object):
    # 禁用或启用访问日志
    ACCESS_LOG = False
    # 控制应用程序是否在文件更改时自动重新加载
    AUTO_RELOAD = False
    # 未捕获和处理异常时的错误响应格式
    FALLBACK_ERROR_FORMAT = "json"
    # 开启keep-alive
    KEEP_ALIVE = True
    # 保持 TCP 连接打开的时间 （秒）
    KEEP_ALIVE_TIMEOUT = 120
    # 请求缓冲区大小
    REQUEST_BUFFER_SIZE = 65536
    # 请求的大小（字节），默认值为 100 MB
    REQUEST_MAX_SIZE = 100000000
    # 请求标头的大小 （字节），默认为 8192 字节
    REQUEST_MAX_HEADER_SIZE = 8192
    # 请求到达需要多长时间 （秒）
    REQUEST_TIMEOUT = 600
    # 响应处理需要多长时间 （秒）
    RESPONSE_TIMEOUT = 600
    # 是否覆盖循环策略, win平台不支持，将设置为False
    USE_UVLOOP = False
    # 程序API基础路径
    API_BASIC_PATH = "api"

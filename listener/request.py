async def before_request(request):
    print("请求处理前执行")
    # 这里可以执行一些请求前的操作，例如验证身份、记录日志等

async def after_request(request, response):
    print("请求处理后执行")
    # 这里可以执行一些请求后的操作，例如记录日志、修改响应等
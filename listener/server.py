async def before_server_start(app, loop):
    print("服务器启动前执行")
    # 这里可以执行一些初始化操作，例如连接数据库、加载配置文件等

async def after_server_start(app, loop):
    print("服务器启动后执行")
    # 这里可以执行一些启动后的操作，例如启动定时任务、发送通知等

async def before_server_stop(app, loop):
    print("服务器停止前执行")
    # 这里可以执行一些清理操作，例如关闭数据库连接、保存状态等

async def after_server_stop(app, loop):
    print("服务器停止后执行")
    # 这里可以执行一些最后的清理操作
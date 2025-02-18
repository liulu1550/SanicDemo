from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound, ServerError

class CustomException(Exception):
    """自定义异常基类"""
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.status_code = status_code
        self.message = message

class UnauthorizedError(CustomException):
    """未授权异常"""
    def __init__(self, message="Unauthorized"):
        super().__init__(message, status_code=401)

class ProxyError(CustomException):
    """代理异常"""
    def __init__(self, message="代理异常"):
        super().__init__(message, status_code=417)

def setup_exception_handlers(app: Sanic):
    """
    设置自定义异常处理器
    """
    @app.exception(CustomException)
    async def handle_custom_exception(request, exception: CustomException):
        """处理自定义异常"""
        return json({
            "code": exception.status_code,
            "data": exception.message,
            "msg": "error"
        }, status=exception.status_code)

    @app.exception(NotFound)
    async def handle_not_found(request, exception):
        """处理 404 异常"""
        return json({
            "code": 404,
            "data": "请求地址非法",
            "msg": "error"
        }, status=404)

    @app.exception(Exception)
    async def handle_generic_exception(request, exception):
        """处理所有未捕获的异常"""
        return json({
            "code": 500,
            "msg": f"服务器错误,错误未捕获: {exception.message}",
            "status": "error"
        }, status=500)

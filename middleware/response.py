import json
import logging

from sanic import Request, HTTPResponse

from middleware.base import BaseMiddleware

logger = logging.getLogger(__name__)


class ResponseMiddleware(BaseMiddleware):
    """中间件"""

    async def before_request(self, request: Request) -> None:
        # 请求前处理
        pass

    async def before_response(self, request: Request, response: HTTPResponse) -> None:
        # 响应前处理
        try:
            if response.content_type == "application/json":
                response_body = json.loads(response.body)
                response_body['path'] = request.path
                response.body = bytes(json.dumps(response_body), 'utf-8')
        except Exception as e:
            logger.error(f"{request.path}的响应处理失败:{e}")
            pass

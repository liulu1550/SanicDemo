from typing import Optional

from curl_cffi import requests
from curl_cffi.requests import BrowserTypeLiteral
from loguru import logger


class CurlClient:
    def __init__(
            self,
            timeout: int = 30,
            proxy: Optional[str] = None
    ):
        self.timeout = timeout
        self.proxy = proxy

    async def _request(
            self,
            method,
            url,
            params: dict = None,
            data: dict = None,
            json: dict = None,
            headers: dict = None,
            proxy: Optional[str] = None,
            allow_redirects: bool = True,
            timeout: int = 30,
            impersonate: Optional[BrowserTypeLiteral] = None
    ):
        try:
            async with requests.AsyncSession(
                    proxy=proxy or self.proxy,
                    allow_redirects=allow_redirects,
                    timeout=timeout or self.timeout,
                    impersonate=impersonate
            ) as client:
                response = await client.request(
                    method=method.upper(),
                    url=url,
                    params=params,
                    headers=headers,
                    data=data,
                    json=json
                )
                return response
        except Exception as e:
            logger.error(f"Request failed: {e}")
            raise e

    async def http_get(
            self, url,
            params: dict = None,
            headers: dict = None,
            proxy: Optional[str] = None,
            allow_redirects: bool = True,
            timeout: int = 30,
            impersonate: Optional[BrowserTypeLiteral] = None
    ):
        """

        :param url: 请求url
        :param params: 请求参数
        :param headers: 请求头
        :param proxy: 请求代理  http://xxx.xxx.xxx.xxx:xxxx
        :param allow_redirects: 允许重定向
        :param timeout: 请求超时时间
        :param impersonate: 浏览器指纹
        :return:
        """
        return await self._request(
            method="GET",
            url=url,
            params=params,
            headers=headers,
            proxy=proxy,
            allow_redirects=allow_redirects,
            timeout=timeout,
            impersonate=impersonate
        )

    async def http_post(self,
                        url,
                        params: dict = None,
                        data: dict = None,
                        json: dict = None,
                        headers: dict = None,
                        proxy: Optional[str] = None,
                        allow_redirects: bool = True,
                        timeout: int = 30,
                        impersonate: Optional[BrowserTypeLiteral] = None
                        ):
        """
        :param url: 请求url
        :param params: 请求参数
        :param data: 请求表单
        :param json: 请求json
        :param headers: 请求头
        :param proxy: 请求代理  http://xxx.xxx.xxx.xxx:xxxx
        :param allow_redirects: 允许重定向
        :param timeout: 请求超时时间
        :param impersonate: 浏览器指纹
        :return:
        """
        return await self._request(
            method="POST",
            url=url,
            params=params,
            data=data,
            json=json,
            headers=headers,
            proxy=proxy,
            allow_redirects=allow_redirects,
            timeout=timeout,
            impersonate=impersonate
        )
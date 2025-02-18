#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：SanicDemo 
@File    ：views.py
@IDE     ：PyCharm 
@Author  ：多点部落
@Date    ：2025/2/18 9:17 
'''
from libs import json_success_response, CurlClient, json_fail_response
from libs.exceptions import CustomException, UnauthorizedError


async def test(request):
    client = CurlClient()
    try:
        res = await client.http_get("http://httpbin.org/get")
    except Exception as e:
        raise CustomException(message=str(e))
    return json_success_response(res.json())
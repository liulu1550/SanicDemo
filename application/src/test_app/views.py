#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：SanicDemo 
@File    ：views.py
@IDE     ：PyCharm 
@Author  ：多点部落
@Date    ：2025/2/18 9:17 
'''
from libs.response import json_success_response

async def test(request):
    return json_success_response()
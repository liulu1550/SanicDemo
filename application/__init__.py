from sanic import Sanic

from application.config import BaseConfig


def create_app():
    """
    创建项目app
    :return:
    """
    app: Sanic = Sanic(__name__)
    app.update_config(BaseConfig)
    # 注册监听
    listener(app)
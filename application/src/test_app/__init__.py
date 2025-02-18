from sanic import Blueprint

from application.src.test_app.views import test

TEST_APP_ROUTER: Blueprint = Blueprint('tetsapp')
TEST_APP_ROUTER.add_route(test, 'test_app/test', name="测试路由1")
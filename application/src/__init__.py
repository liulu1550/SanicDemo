import importlib
import os

from sanic import Blueprint, Sanic

base_path = "application/src"
base_import = "application.src"


def list_directories() -> list:
    # 获取目录下的所有文件和文件夹
    path = base_path
    return [entry.name for entry in os.scandir(path) if entry.is_dir() and entry.name != '__pycache__']


def import_routers(base_path: str, base_import: str) -> dict:
    """
    动态导入指定目录中的模块，并提取变量。
    """
    routers = {}
    for entry in os.scandir(base_path):
        if entry.is_dir() and entry.name != '__pycache__':
            module_name = f"{base_import}.{entry.name}"  # 构造模块路径
            variable_name = f"{entry.name.upper()}_ROUTER"  # 根据文件夹名构造大写的变量名
            try:
                # 动态导入模块
                module = importlib.import_module(module_name)
                # 获取模块中的变量
                if hasattr(module, variable_name):
                    routers[variable_name] = getattr(module, variable_name)
                else:
                    print(f"{module_name} does not contain {variable_name}.")
            except (ModuleNotFoundError, AttributeError) as e:
                print(f"Error importing {module_name}: {e}")
    return routers


# 获取 routers
routers = import_routers(base_path, base_import)
APP_BLUE_TUPLE: tuple[Blueprint, ...] = tuple(routers.values())


def register_blueprint(app: Sanic):
    """
    注册蓝图
    :param app:
    :return:
    """
    for blueprint in APP_BLUE_TUPLE:
        app.blueprint(blueprint, url_prefix=f"/{app.config.get('API_BASIC_PATH')}")
    return None

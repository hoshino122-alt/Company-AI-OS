import importlib
import inspect
import pkgutil

import tools


TOOLS = {}


def register_tool(name, function):
    TOOLS[name] = function


def has_tool(name):
    return name in TOOLS


def run_tool(name, *args, **kwargs):

    if not has_tool(name):
        return "許可されていないToolです。"

    return TOOLS[name](*args, **kwargs)


def get_tool_list():
    return list(TOOLS.keys())


def get_tool_descriptions():

    descriptions = {}

    for name, function in TOOLS.items():

        descriptions[name] = function.__doc__ or "説明なし"

    return descriptions


def load_tools():
    for module_info in pkgutil.iter_modules(tools.__path__):
        module_name = module_info.name

        if module_name.startswith("_"):
            continue

        if not module_name.endswith("_tool"):
            continue

        try:
            module = importlib.import_module(
                f"tools.{module_name}"
            )
        except Exception as exc:
            print(
                f"Toolの読み込みをスキップ: "
                f"{module_name} "
                f"({type(exc).__name__}: {exc})"
            )
            continue

        for name, obj in inspect.getmembers(
            module,
            inspect.isfunction
        ):
            if obj.__module__ == module.__name__ and not name.startswith("_"):
                register_tool(name, obj)

load_tools()
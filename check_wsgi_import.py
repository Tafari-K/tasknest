import importlib, traceback

try:
    importlib.import_module('tasknest_project.wsgi')
    print('wsgi import ok')
except Exception:
    traceback.print_exc()

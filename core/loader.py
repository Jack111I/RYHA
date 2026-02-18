import types, base64

def execute_in_memory(module_name, b64_code):
    """Executes a module without saving it to a file"""
    code = base64.b64decode(b64_code).decode()
    module = types.ModuleType(module_name)
    exec(code, module.__dict__)
    return module.run()
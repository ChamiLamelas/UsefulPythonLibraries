import inspect

def get_caller():
    return inspect.stack()[1].function

def get_func_byname(module, func_name, substitute):
    """Gets function object by name from module object, errors are thrown if a function with that name cannot be created"""

    if not hasattr(module, func_name):
        return substitute
    func = getattr(module, func_name)
    if not inspect.isfunction(func):
        return substitute

    # Note this does not check if the function takes a single parameter, but we assume that a user could
    # figure this out from the traceback who is comfortable enough with Python to write a custom function
    # to pass in here
    return func

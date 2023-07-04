def func_decoration(func):
    def wrapper(*args, **kwargs):
        print('it is fun')
        res = func(*args, **kwargs)
        print(f'something')
        return res

    return wrapper


def some_func(x, y):
    z = x / y
    return z


some_func = func_decoration(some_func)
res = some_func(1000, 2)
print(res)
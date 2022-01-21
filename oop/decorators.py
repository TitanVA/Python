import math
from functools import wraps


def burger_decorator(func):
    def wrapper(*args, **kwargs):
        print("{¯¯¯¯¯¯¯¯}")
        print("Булка")
        print("-" * 10)
        func(*args, **kwargs)
        print("-" * 10)
        print("Соус")
        print("Булка")
        print("{________}")

    return wrapper


@burger_decorator
def ingredients(*args, **kwargs):
    for arg in args:
        print(arg)


# burger = ingredients("Котлета", "Огурец", "Сыр")


#  Декоратор с параметрами
def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper

    return func_decorator


@df_decorator(dx=0.0001)
def sin_df(x):
    return math.sin(x)


df = sin_df(math.pi / 3)


# print(df)


def decorator_function(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        print("Wrapper")
        return func(*args, **kwargs)

    return wrapper_function


def display():
    print("Display function ran")


decorated_display = decorator_function(display)
# decorated_display()
print(decorated_display.__name__)


class DecoratorClass:
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("Call method")
        return self.original_func(*args, **kwargs)


@DecoratorClass
def display():
    print("Display function")


@DecoratorClass
def display_info(name, age):
    print(f"Display info {name} {age}")


d1 = display_info("Viktor", 33)

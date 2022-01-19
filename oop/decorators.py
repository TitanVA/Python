def burger_decorator(func):
    def wrapper(*args, **kwargs):
        print("{¯¯¯¯¯¯¯¯}")
        print("Булка")
        print("-"*10)
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


burger = ingredients("Котлета", "Огурец", "Сыр")

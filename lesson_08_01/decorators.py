from abc import ABC, abstractmethod
import time


class Interface(ABC):

    @abstractmethod
    def __call__(self):
        pass


class Example(Interface):

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self):
        return self.arg1 + self.arg2


class Wrapper(Interface):

    def __init__(self, wrapee):
        self.wrapee = wrapee

    def __call__(self):
        result = self.wrapee()
        return result * 2


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function {func.__name__} took {end_time - start_time} seconds')
        return result
    return wrapper


@time_decorator
def fun(arg):
    res = 1
    for i in range(arg):
        res *= 50
    return res


def add_two(arg1, arg2):
    return arg1 + arg2


n = lambda x: x + 1


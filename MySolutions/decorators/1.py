# https://www.w3resource.com/python-exercises/decorator/index.php


def decorator_function(f):
    def wrapped_function(*args, **kwargs):
        print(f"Arguments: {args}") 
        return f(*args,**kwargs) 
    return wrapped_function


@decorator_function
def add(x, y):
    return x + y

@decorator_function
def add_3(x, y, k):
    return x + y + k


print(add(5, 3))
print(add_3(5, 3, 10))

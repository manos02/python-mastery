# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)
   
    return value

class TypedProperty:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        setattr(instance, self.private_name, value)

String = lambda x: typedproperty(x, str)
Integer = lambda x: typedproperty(x, int)
Float = lambda x: typedproperty(x, float)

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stock(name="test-name", shares=5, price=10.5)

String = TypedProperty(str)
Integer = TypedProperty(int)
Float = TypedProperty(float)

class Stock1:
    name = String
    shares = Integer
    price = Float

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s1 = Stock1(name="test-name", shares=5, price=10.5)


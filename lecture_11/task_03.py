class MyClass:
    """About class"""
    A = 42

    def __init__(self, a, b):
        """self.__doc__ = None"""
        self.a = a
        self.b = b

    # def method(self):
    #     """Documentation"""
    #     self.__doc__ = None
    #     help(MyClass)

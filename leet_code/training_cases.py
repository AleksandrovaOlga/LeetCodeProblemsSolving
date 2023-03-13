"""
This module contains examples of functions, classe, etc.
@author: Olushka
@licence: MIT
"""
from typing import Tuple, List

import abc


class MyInterface(abc.ABC):
    def __init__(self, a):
        self.a = a

    @abc.abstractmethod
    def my_method(self):
        """Delaet horosho"""
        ...

    def call_my_method(self):
        return self.my_method()


class MyREALClass(MyInterface, OTHERCLASS):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
        self._d = 6
        self.__e = 5

    def my_method(self):
        print("qq")

    def call_my_method(self):
        print("not qq")
        super().call_my_method()

    def __getitem__(self, name):
        if name == "b":
            return self.b
        return 1

    def __class_getitem__(cls, item):
        return None


class MyREALClass2(MyInterface):
    def my_method(self):
        print("zz")


def super_func(param: MyInterface) -> None:
    param.my_method()


if __name__ == "__main__":
    a = MyREALClass(1, 2)
    a.call_my_method()
    print(a["b"], MyREALClass[int])
    super_func(a)
    b: List[int] = []
    a._d = 6

class A:
    def class_method(self):
        print("method in class:B")

class B:
    def calss_method(self):
        print("method in class:B")

class C:
    def __class__(self):
        print("method in class:C")

class D(B,C):
    pass
d=D()
d.calss_method()
print(f"method resolution:{D.__mro__}")
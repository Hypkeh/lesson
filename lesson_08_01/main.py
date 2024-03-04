
class A:
    def a(self):
        print('a')


class B(A):

    def a(self):
        print('b')

b = B()
b.a()

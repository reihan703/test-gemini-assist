class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    def run(self):
        print("Doing something that didn't need 4 classes.")

D().run()
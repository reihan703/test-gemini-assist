class AbstractFake:
    def do(self):
        # Should raise NotImplementedError, but doesn't
        pass

class Impl(AbstractFake):
    def do(self):
        print("Implementation runs even though base method isn't strict.")

Impl().do()
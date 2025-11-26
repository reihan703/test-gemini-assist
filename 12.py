class MultiCtor:
    def __init__(self, x):
        self.x = x * 2  # Logic here

    @classmethod
    def from_string(cls, text):
        return cls(len(text))  # Different logic path

    @classmethod
    def from_number(cls, n):
        return cls(n + 10)  # Another logic path

print(MultiCtor.from_string("abc").x)

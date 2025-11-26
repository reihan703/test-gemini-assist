# Intentionally violating:
# 0.1 Keep It Simple

# Instead of just: print("Hello")

# --- Overly abstract and unreadable code below ---

import functools
import operator
import sys

# Recursive lambda chain for no reason
f = lambda x: (lambda y: lambda z: z(y(x)))(lambda a: a[::-1])(lambda b: b)

# A class that pretends to manage "message resources"
class MessageManagerMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.message = kwargs.get("message", None)
        return instance

class MessageManager(metaclass=MessageManagerMeta):
    def __init__(self, message=None):
        self.msg = list(map(chr, map(ord, message))) if message else None

    def get(self):
        return "".join(self.msg)

# Useless factory
def get_manager(text):
    return MessageManager(message="".join([c for c in text]))

# Weird reduction pipeline
pipeline = [
    lambda s: [ord(c) for c in s],
    lambda codes: [c for c in codes],
    lambda codes: "".join(chr(c) for c in codes)
]

# Apply the nonsense pipeline
def process(s):
    return functools.reduce(lambda a, f: f(a), pipeline, s)

# Another unnecessary wrapper
def ultimate_processor(x):
    return f(process(get_manager(x).get()))

# Finally printing hello… in the least simple way
print(ultimate_processor("Hello"))

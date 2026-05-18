from .m1 import *

globals()["__i"] = vars(__import__("pkg.m1", fromlist=["*"]))["__i"]

__all__ = ["pi", "__i"]

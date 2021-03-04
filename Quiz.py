"""XYZ 123."""

a: str = "x"
b: str = "y" + a + "y"
c: str = "z" + b + "z"
n: int = len(c)
print(c[n - 1])
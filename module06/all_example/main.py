from shapes import *

# These work — all listed in __all__
print(circle_area(5))       # 78.53...
print(circumference(5))     # 31.41...
print(rect_area(4, 6))      # 24
print(perimeter(4, 6))      # 20

# This would raise NameError — _validate is private (not in __all__)
# print(_validate(5))

# You can still import it explicitly by name even if not in __all__
from shapes.circle import _validate
_validate(5)
print("explicit import of private name works:", _validate)

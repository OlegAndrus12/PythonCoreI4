from .circle import area as circle_area, circumference
from .rectangle import area as rect_area, perimeter

# __all__ defines the public API of this package.
# Only these names are exported when someone does: from shapes import *
# The private helpers (_validate in each module) are excluded automatically
# because they start with underscore, but __all__ also excludes anything
# not listed — even public names that weren't imported here.
__all__ = [
    "circle_area",
    "circumference",
    "rect_area",
    "perimeter",
]

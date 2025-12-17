from enum import Enum


class Stack(Enum):
    STANDARD = 'standard'
    SPECIAL = 'special'
    REJECTED = 'rejected'


class PackageType(Enum):
    BULKY = 'bulky'
    HEAVY = 'heavy'
    BOTH = 'both'
    NONE = 'none'

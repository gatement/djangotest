from enum import Enum, unique

@unique
class Lgh(Enum):
    v1 = 1
    v2 = "1"

print Lgh.v1.name, Lgh.v1.value
print Lgh.v2.name, Lgh.v2.value

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    BLACK = 1

print(Color.BLACK.name)
result = Color.RED == Color.GREEN
print(result)

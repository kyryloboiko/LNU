from math import sqrt

# Базовий клас Figure, створений динамічно через type()
Figure = type(
    'Figure',
    (object,),
    {
        '__init__': lambda self, a, b=None: setattr(
            self,
            '__dict__',
            {'a': a, 'b': b, 'name': self.__class__.__name__}
        ),
        '__str__': lambda self: f'{self.name} Дарина\n{self.name} Периметр/Довжина: {self.perimetr()}\n{self.name} Площа: {self.area()}',
    },
)

# Клас Коло
Circle = type(
    'Circle',
    (Figure,),
    {
        'area': lambda self: 3.14 * self.a**2,
        'perimetr': lambda self: 2 * 3.14 * self.a,
    },
)

# Клас Трикутник
Triangle = type(
    'Triangle',
    (Figure,),
    {
        'area': lambda self: (sqrt(3) / 4) * self.a**2,
        'perimetr': lambda self: self.a * 3,
    },
)

# Клас Прямокутник
Square = type(
    'Square',
    (Figure,),
    {
        'area': lambda self: self.a * self.b,
        'perimetr': lambda self: 2 * (self.a + self.b),
    },
)

# Функція, яка створює об'єкти і викликає їх методи
def func():
    obja = Circle(2)
    objb = Square(3, 5)
    objc = Triangle(5)

    for obj in (obja, objb, objc):
        print(obj)

# Точка входу в програму
if __name__ == '__main__':
    func()

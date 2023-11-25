from attr.exceptions import FrozenInstanceError
from attrs import asdict, define, field, frozen


@define
class Animal:
    """Пример класса.

    Поля заданы с использованием значений по умолчанию, приведение типа данных.
    Применен простой валидатор.
    """
    name: str = field()
    weigh: int = field(converter=int)
    allowed_food: list = field(default=[])

    @weigh.validator
    def _check_weigh(self, attribute, value):
        if value <= 0:
            raise ValueError("Неверно указан вес животного.")


@frozen
class Box:
    """Пример класса, объекты которого будут неизменяемы."""
    width: int
    height: int


animal_1 = Animal(name='Барсик', weigh='20')
animal_2 = Animal(name='Барсик', weigh='20')

# Читаемый вывод объекта
print(animal_1)

# Сравнение объектов
print(animal_1 == animal_2)

# Превратим объект в словарь
print(asdict(animal_1))

# Пример неизменяемых объектов
box = Box(10, 6)
try:
    box.height = 8
except FrozenInstanceError as e:
    print(f'Ошибка: {e.msg}')

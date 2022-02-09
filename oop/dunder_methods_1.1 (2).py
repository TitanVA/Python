class Employee:
    count_of_objects = 0
    max_objects = 3

    def __new__(cls, *args, **kwargs):
        """Вызывается перед созданием объекта класса"""
        if cls.count_of_objects < cls.max_objects:  # если количество экземпляров больше максимального, не создаем новый
            cls.count_of_objects += 1
            return super().__new__(cls)
        else:
            return None

    def __init__(self, first_name: str, last_name: str, level: int, salary: float, resume=None):
        """Вызывается сразу после создания объекта класса"""
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.salary = salary
        self.resume = resume
        self.employee = [self.first_name, self.last_name, self.level,
                         self.salary]  # для дальнейшего итерирования и индексации
        self._count = -1  # в итерировании использую для индекса

    @classmethod
    def remove_object(cls):
        cls.count_of_objects -= 1  # отнимаем от количества экземпляров

    @staticmethod
    def levels() -> dict: # обозначение уровней сотрудника
        description = {
            0: "Trainee",
            1: "Junior",
            2: "Middle",
            3: "Senior",
        }
        return description

    def level_description(self, value): # описание уровня
        return self.levels().get(value, None)

    def __del__(self):
        self.remove_object()
        del self

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.level == other.level  # сравниваю level работников
        else:
            return f"Невозможно сравнить с {other}"

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.level < other.level  # сравниваю level работников
        elif isinstance(other, (int, float)):
            return self.level < other
        else:
            return f"Невозможно сравнить с {other}"

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.level > other.level  # сравниваю level работников
        elif isinstance(other, (int, float)):
            return self.level > other
        else:
            return f"Невозможно сравнить с {other}"

    def __repr__(self):
        return f"{self.first_name};{self.last_name};{self.level};{self.salary};{self.resume}"

    def __str__(self):
        return f"Сотрудник {self.first_name} {self.last_name}"

    def __iter__(self):
        return iter(self.employee)

    def __next__(self):
        self._count += 1
        if self._count < len(self):
            return self.employee[self._count]
        else:
            raise StopIteration

    def __enter__(self):
        if self.resume:
            self.file = open(self.resume, "r")
            return self.file
        else:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def __len__(self):
        return len(self.employee)

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary  # возвращаю сумму salary
        elif isinstance(other, (int, float)):
            return self.salary + other
        else:
            return f"Невозможно сложить с {other}"

    def __mul__(self, other):
        if isinstance(other, Employee):
            return self.salary * other.salary  # возвращаю умножение salary
        elif isinstance(other, (int, float)):
            return self.salary * other
        else:
            return f"Невозможно умножить на {other}"

    def __call__(self, *args, **kwargs):
        print(self)
        print(f"Вас вызывает начальство")
        print("-" * 30)

    def __get__(self, instance, owner):
        return f"{self.first_name} {self.last_name}"

    def __getitem__(self, item):
        if 0 <= item < len(self.employee):
            return self.employee[item]
        else:
            raise IndexError("Индекс за границами элемента")

    def __getattribute__(self, item):  # запрещаем доступ напрямую к max_objects
        if item == "max_objects":
            raise ValueError("Доступ запрещен")
        else:
            return super().__getattribute__(item)

    @property
    def level(self):
        """Возвращение level сотрудника"""
        return self.__level

    @level.setter
    def level(self, value):
        """Сеттер для level"""
        if value in self.levels():
            self.__level = value
        else:
            raise ValueError("Такого уровня нет")


viktor = Employee("Viktor", "Bezai", 0, 100, resume="viktor.txt")
oleg = Employee("Oleg", "Ivanov", 2, 500)
print(viktor.level)
viktor.level = 1
print(viktor.level)
print(next(viktor))
print(next(viktor))
print(next(viktor))
print(next(viktor))
print(viktor > oleg)
print(oleg > viktor)
print(oleg + viktor)
with viktor as file:
    print(file.readlines())
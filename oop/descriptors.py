class PositiveInteger:
    def __get__(self, instance, owner):
        return getattr(instance, self.var_name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError()
        setattr(instance, self.var_name, value)

    def __set_name__(self, owner, name):
        self.var_name = "_" + name


class OnlyLetters:
    def __get__(self, instance, owner):
        return getattr(instance, self.var_name)

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError()
        setattr(instance, self.var_name, value)

    def __set_name__(self, owner, name):
        self.var_name = "_" + name


class Employee:
    first_name = OnlyLetters()
    last_name = OnlyLetters()
    level = PositiveInteger()
    salary = PositiveInteger()

    def __str__(self):
        return f"{self.first_name};{self.last_name};{self.level};{self.salary}"


viktor = Employee()
viktor.first_name = "Viktor"
viktor.last_name = "Bezai"
viktor.level = 2
viktor.salary = 200
print(viktor)
oleg = Employee()
oleg.first_name = "Oleg"
oleg.last_name = "Ivanov"
oleg.level = 3
oleg.salary = 300
print(oleg)
